import streamlit as st
import os
import pandas as pd
from datetime import date
from db.sqlite_manager import SQLiteManager
from core.ai_engine import AIEngine
from core.afa_generator import AFAGenerator

def render():
    st.markdown("<h2 style='color:#0F2C59;'>⚙️ Nuevo Análisis de Falla (AFA / FMEA - Estándar MAN-F-054)</h2>", unsafe_allow_html=True)
    st.caption("Complete la información básica. La Inteligencia Artificial generará el análisis de ingeniería completo, el desglose 5W+2H, los 5 Porqués y los planes de acción según el formato oficial.")

    with st.form("afa_form"):
        col_hdr1, col_hdr2 = st.columns(2)
        with col_hdr1:
            title = st.text_input("1. Título del Análisis de Falla")
            leader = st.text_input("Líder del AFA", value="Especialista en Confiabilidad")
            area = st.selectbox("Área / Sistema", ["Mantenimiento", "Operaciones", "Procesos", "Calidad", "Confiabilidad"])
            equipment = st.text_input("Equipo / Componente / Tag")
        with col_hdr2:
            event_date = st.date_input("Fecha", value=date.today())
            participants = st.text_input("Participantes del Equipo", value="Ing. de Mantenimiento, Supervisor de Operaciones, Técnico Mecánico")
            linea = st.text_input("Línea de Producción / Sistema")
            criticality = st.selectbox("Criticidad de la Falla", ["Alta", "Media", "Baja"])

        description = st.text_area("2. Descripción del Modo de Falla y Síntomas Observados")

        st.markdown("### 📎 Evidencias e Información Adjunta (Fotos, Planos, Manuales, TXT)")
        uploaded_files = st.file_uploader(
            "Adjunte evidencias (imágenes, planos, manuales o archivos .TXT / .MD):",
            accept_multiple_files=True
        )

        submitted = st.form_submit_button("⚙️ Generar AFA Completo con IA Industrial")

        if submitted:
            if not title or not description:
                st.error("Por favor complete al menos el título y la descripción del modo de falla.")
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
                        description=description, leader=leader, participants=participants,
                        username=st.session_state.get("username", "admin"),
                        attachments_text=attachments_text
                    )
                st.success(f"¡AFA generado con éxito! ID de Evento: #{event_id}. Archivos analizados: {evidence_count}.")
                
                # Despliegue en pantalla completo
                st.markdown("---")
                st.markdown("### 📋 REPORTE OFICIAL AFA - ESTÁNDAR MAN-F-054")
                afa_data = db.execute_query("SELECT * FROM afa WHERE event_id = ?", (event_id,))
                actions_data = db.execute_query("SELECT * FROM actions WHERE event_id = ?", (event_id,))
                
                if afa_data:
                    afa = dict(afa_data[0])
                    st.markdown("#### 1. Datos Generales del Análisis AFA")
                    st.write(f"• **Líder AFA:** {afa.get('leader', '')} | **Participantes:** {afa.get('participants', '')}")
                    st.write(f"• **Área/Equipo:** {area} - {equipment} | **Línea:** {linea}")

                    st.markdown("#### 2. Enfoque del Problema y Modo de Falla (5W + 2H)")
                    st.info(f"**Modo de Falla Técnico:** {afa.get('failure_mode', '')}")
                    st.write(f"• **Efecto en Sistema:** {afa.get('effect', '')}")
                    st.write(f"• **Consecuencia:** {afa.get('consequence', '')}")
                    
                    c_5w1, c_5w2 = st.columns(2)
                    with c_5w1:
                        st.write(f"• **¿Qué pasó?:** {afa.get('what_happened', '')}")
                        st.write(f"• **¿Cómo ocurrió?:** {afa.get('how_happened', '')}")
                        st.write(f"• **¿Quién detectó?:** {afa.get('who_detected', '')}")
                        st.write(f"• **¿Cuánto (Pérdida)?:** {afa.get('how_much_loss', '')}")
                    with c_5w2:
                        st.write(f"• **¿Cuál material/componente?:** {afa.get('which_materials', '')}")
                        st.write(f"• **¿Dónde nació la falla?:** {afa.get('where_located', '')}")
                        st.write(f"• **¿Cuándo inició?:** {afa.get('when_started', '')}")
                        st.write(f"• **Acción Inmediata:** {afa.get('immediate_action', '')}")

                    st.markdown("#### 3. Análisis COMPLETO de los 5 Porqués (AFA)")
                    st.write(f"1. **¿Por qué 1?:** {afa.get('why_1', '')}")
                    st.write(f"2. **¿Por qué 2?:** {afa.get('why_2', '')}")
                    st.write(f"3. **¿Por qué 3?:** {afa.get('why_3', '')}")
                    st.write(f"4. **¿Por qué 4?:** {afa.get('why_4', '')}")
                    st.write(f"5. **¿Por qué 5 (Causa Raíz):** {afa.get('why_5', '')}")
                    
                    st.markdown("#### 4. Determinación de Causas y Conclusiones")
                    st.write(f"• **Causa Física Directa:** {afa.get('physical_cause', '')}")
                    st.write(f"• **Causa Contribuyente:** {afa.get('contributor_cause', '')}")
                    st.write(f"• **Causa Raíz Sistémica:** {afa.get('root_cause', '')}")

                    st.markdown("#### 5. Plan de Acción AFA MAN-F-054")
                    st.dataframe(pd.DataFrame([dict(a) for a in actions_data]), use_container_width=True)
                st.balloons()
