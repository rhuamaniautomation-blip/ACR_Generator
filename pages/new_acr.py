import streamlit as st
import os
import pandas as pd
from datetime import date
from db.sqlite_manager import SQLiteManager
from core.ai_engine import AIEngine
from core.rca_generator import RCAGenerator

def render():
    st.markdown("<h2 style='color:#0F2C59;'>📝 Nuevo Análisis de Causa Raíz (ACR - Estándar MAN-F-054)</h2>", unsafe_allow_html=True)
    st.caption("Complete la información general e inicial. La IA completará automáticamente todos los campos del formato oficial MAN-F-054, el árbol de 5 Porqués y los planes de acción.")

    with st.form("acr_form"):
        col_hdr1, col_hdr2 = st.columns(2)
        with col_hdr1:
            title = st.text_input("1. Título del Evento / Problema")
            leader = st.text_input("Líder del ACR", value="Ing. Confiabilidad")
            area = st.selectbox("Área / Planta", ["Mantenimiento", "Operaciones", "Procesos", "Calidad", "Cadena de Suministro"])
            equipment = st.text_input("Equipo / Tag / Activo")
        with col_hdr2:
            event_date = st.date_input("Fecha de Análisis", value=date.today())
            participants = st.text_input("Participantes del Equipo", value="Sup. Mantenimiento, Operador de Estación, Especialista RCM")
            linea = st.text_input("Línea de Producción / Sistema")
            criticality = st.selectbox("Criticidad del Evento", ["Alta", "Media", "Baja"])

        description = st.text_area("2. Descripción Inicial del Problema", help="Describa el fallo, la condición observada o el síntoma técnico.")

        st.markdown("### 📎 Evidencias e Información Adjunta (Fotos, Planos, Manuales, TXT)")
        uploaded_files = st.file_uploader(
            "Adjunte evidencias (imágenes, planos, manuales o archivos .TXT / .MD):",
            accept_multiple_files=True
        )

        submitted = st.form_submit_button("⚙️ Generar ACR Completo con IA Industrial")

        if submitted:
            if not title or not description:
                st.error("Por favor complete al menos el título y la descripción del evento.")
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
                rca_gen = RCAGenerator(db, ai)
                with st.spinner("Ejecutando análisis técnico de ingeniería bajo Estándar MAN-F-054..."):
                    event_id = rca_gen.process_acr(
                        title=title, event_date=str(event_date), area=area,
                        linea=linea, equipment=equipment, criticality=criticality,
                        description=description, leader=leader, participants=participants,
                        username=st.session_state.get("username", "admin"),
                        attachments_text=attachments_text
                    )
                st.success(f"¡Análisis ACR generado exitosamente! ID de Registro: #{event_id}. Archivos procesados: {evidence_count}.")
                
                # Despliegue en pantalla del estándar MAN-F-054
                st.markdown("---")
                st.markdown("### 📋 REPORTE OFICIAL ACR - ESTÁNDAR MAN-F-054")
                acr_data = db.execute_query("SELECT * FROM acr WHERE event_id = ?", (event_id,))
                actions_data = db.execute_query("SELECT * FROM actions WHERE event_id = ?", (event_id,))
                
                if acr_data:
                    acr = dict(acr_data[0])
                    
                    st.markdown("#### 1. Datos Generales del Análisis")
                    st.write(f"• **Líder del ACR:** {acr.get('leader', '')} | **Participantes:** {acr.get('participants', '')}")
                    st.write(f"• **Área/Equipo:** {area} - {equipment} | **Línea:** {linea}")

                    st.markdown("#### 2. Enfoque del Problema (Desglose 5W + 2H)")
                    st.info(f"**Problema Enfocado:** {acr.get('problem_definition', '')}")
                    c_5w1, c_5w2 = st.columns(2)
                    with c_5w1:
                        st.write(f"• **¿Qué pasó?:** {acr.get('what_happened', '')}")
                        st.write(f"• **¿Cómo ocurrió?:** {acr.get('how_happened', '')}")
                        st.write(f"• **¿Quién detectó?:** {acr.get('who_detected', '')}")
                        st.write(f"• **¿Cuánto (Pérdida)?:** {acr.get('how_much_loss', '')}")
                    with c_5w2:
                        st.write(f"• **¿Cuál material/componente?:** {acr.get('which_materials', '')}")
                        st.write(f"• **¿Dónde nació la falla?:** {acr.get('where_located', '')}")
                        st.write(f"• **¿Cuándo inició?:** {acr.get('when_started', '')}")
                        st.write(f"• **Acción Inmediata:** {acr.get('immediate_action', '')}")

                    st.markdown("#### 3. Análisis de los 5 Porqués (Causa Raíz de Ingeniería)")
                    st.write(f"1. **¿Por qué 1?:** {acr.get('why_1', '')}")
                    st.write(f"2. **¿Por qué 2?:** {acr.get('why_2', '')}")
                    st.write(f"3. **¿Por qué 3?:** {acr.get('why_3', '')}")
                    st.write(f"4. **¿Por qué 4?:** {acr.get('why_4', '')}")
                    st.write(f"5. **¿Por qué 5 (Causa Raíz Sistémica):** {acr.get('why_5', '')}")

                    st.markdown("#### 4. Determinación de Causas y Conclusiones")
                    st.write(f"• **Causa Física Directa:** {acr.get('physical_cause', '')}")
                    st.write(f"• **Causa Contribuyente:** {acr.get('contributor_cause', '')}")
                    st.write(f"• **Causa Raíz Sistémica:** {acr.get('root_cause', '')}")

                    st.markdown("#### 5. Plan de Acción y Seguimiento MAN-F-054")
                    st.dataframe(pd.DataFrame([dict(a) for a in actions_data]), use_container_width=True)
                st.balloons()
