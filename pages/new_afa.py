import streamlit as st
import pandas as pd
import os
from datetime import date
from db.sqlite_manager import SQLiteManager
from core.ai_engine import AIEngine
from core.afa_generator import AFAGenerator

def render():
    st.subheader("⚙️ Nuevo Análisis de Falla (AFA / FMEA - Estándar MAN-F-054)")
    
    with st.form("afa_form"):
        title = st.text_input("Título del Análisis de Falla")
        event_date = st.date_input("Fecha", value=date.today())
        area = st.selectbox("Área", ["Mantenimiento", "Operaciones", "Procesos", "Calidad", "Confiabilidad"])
        linea = st.text_input("Línea / Sistema")
        equipment = st.text_input("Equipo / Componente")
        criticality = st.selectbox("Criticidad", ["Alta", "Media", "Baja"])
        description = st.text_area("Descripción del Modo de Falla y Síntomas")
        
        st.markdown("### 📎 Carga de Evidencias y Documentos (Fotos, Planos, Manuales, TXT)")
        uploaded_files = st.file_uploader(
            "Adjunte evidencias (imágenes, manuales, planos o archivos de texto .ZIP/.TXT/.MD):",
            accept_multiple_files=True
        )

        submitted = st.form_submit_button("Generar AFA con IA")

        if submitted:
            if not title or not description:
                st.error("Complete título y descripción.")
            else:
                attachments_text = ""
                evidence_count = 0
                if uploaded_files:
                    upload_dir = os.path.join("database", "uploads")
                    os.makedirs(upload_dir, exist_ok=True)
                    for f in uploaded_files:
                        file_path = os.path.join(upload_dir, f.name)
                        bytes_data = f.read()
                        with open(file_path, "wb") as out_file:
                            out_file.write(bytes_data)
                        evidence_count += 1
                        
                        # Lectura segura de texto si es un archivo .txt, .md o .log
                        if f.name.endswith(".txt") or f.name.endswith(".md") or f.name.endswith(".log"):
                            try:
                                content = bytes_data.decode("utf-8", errors="ignore")
                                attachments_text += f"\n--- Archivo Adjunto: {f.name} ---\n{content[:2000]}\n"
                            except Exception:
                                pass
                        else:
                            attachments_text += f"\n--- Archivo Adjunto (Imagen/Plano/Manual): {f.name} (Registrado para análisis) ---\n"

                db = SQLiteManager()
                ai = AIEngine(provider="Gemini Flash")
                afa_gen = AFAGenerator(db, ai)
                with st.spinner("Ejecutando AFA y análisis completo de 5 Porqués bajo MAN-F-054..."):
                    event_id = afa_gen.process_afa(
                        title=title, event_date=str(event_date), area=area,
                        linea=linea, equipment=equipment, criticality=criticality,
                        description=description, username=st.session_state.get("username", "admin"),
                        attachments_text=attachments_text
                    )
                st.success(f"¡AFA generado con éxito! ID de Evento: #{event_id}. Archivos analizados: {evidence_count}.")
                
                # Mostrar resultado en pantalla inmediatamente
                st.markdown("---")
                st.markdown("### 📋 Resultado del Análisis AFA Generado (Formato MAN-F-054)")
                afa_data = db.execute_query("SELECT * FROM afa WHERE event_id = ?", (event_id,))
                actions_data = db.execute_query("SELECT * FROM actions WHERE event_id = ?", (event_id,))
                if afa_data:
                    afa = dict(afa_data[0])
                    st.info(f"**Modo de Falla:** {afa.get('failure_mode', '')}")
                    st.write(f"**Efecto en el Sistema:** {afa.get('effect', '')}")
                    st.write(f"**Consecuencia:** {afa.get('consequence', '')}")
                    
                    st.markdown("#### Análisis COMPLETO de los 5 Porqués (AFA)")
                    st.write(f"1. **¿Por qué 1?:** {afa.get('why_1', '')}")
                    st.write(f"2. **¿Por qué 2?:** {afa.get('why_2', '')}")
                    st.write(f"3. **¿Por qué 3?:** {afa.get('why_3', '')}")
                    st.write(f"4. **¿Por qué 4?:** {afa.get('why_4', '')}")
                    st.write(f"5. **¿Por qué 5 (Causa Raíz):** {afa.get('why_5', '')}")
                    
                    st.markdown("#### Causa Raíz Fundamental")
                    st.write(f"**Causa Raíz:** {afa.get('root_cause', '')}")

                    st.markdown("#### Plan de Acción AFA")
                    st.dataframe(pd.DataFrame([dict(a) for a in actions_data]), use_container_width=True)
                st.balloons()
