import streamlit as st
import zipfile
import os
from datetime import date
from db.sqlite_manager import SQLiteManager
from core.ai_engine import AIEngine
from core.rca_generator import RCAGenerator

def render():
    st.subheader("📝 Nuevo Análisis de Causa Raíz (ACR - 5W+2H)")
    
    with st.form("acr_form"):
        title = st.text_input("Título del Evento")
        event_date = st.date_input("Fecha del Evento", value=date.today())
        area = st.selectbox("Área", ["Mantenimiento", "Operaciones", "Procesos", "Calidad", "Cadena de Suministro"])
        linea = st.text_input("Línea de Producción / Planta")
        equipment = st.text_input("Equipo / Tag / Activo")
        criticality = st.selectbox("Criticidad", ["Alta", "Media", "Baja"])
        description = st.text_area("Descripción detallada del evento")
        
        st.markdown("### 📎 Carga de Evidencias e Imágenes")
        uploaded_files = st.file_uploader(
            "Seleccione múltiples archivos o un archivo comprimido .ZIP con evidencias:",
            accept_multiple_files=True
        )
        
        submitted = st.form_submit_button("Generar ACR con IA Industrial")

        if submitted:
            if not title or not description:
                st.error("Complete título y descripción.")
            else:
                evidence_count = 0
                if uploaded_files:
                    upload_dir = os.path.join("database", "uploads")
                    os.makedirs(upload_dir, exist_ok=True)
                    for f in uploaded_files:
                        if f.name.endswith(".zip"):
                            with zipfile.ZipFile(f, 'r') as zip_ref:
                                zip_ref.extractall(upload_dir)
                                evidence_count += len(zip_ref.namelist())
                        else:
                            file_path = os.path.join(upload_dir, f.name)
                            with open(file_path, "wb") as out_file:
                                out_file.write(f.getbuffer())
                            evidence_count += 1

                db = SQLiteManager()
                ai = AIEngine(provider="Gemini Flash")
                rca_gen = RCAGenerator(db, ai)
                with st.spinner("Ejecutando análisis de causa raíz..."):
                    event_id = rca_gen.process_acr(
                        title=title, event_date=str(event_date), area=area,
                        linea=linea, equipment=equipment, criticality=criticality,
                        description=description, username=st.session_state.get("username", "admin")
                    )
                st.success(f"¡ACR generado con éxito! ID de Evento: #{event_id}. Archivos de evidencia guardados: {evidence_count}.")
                st.balloons()

