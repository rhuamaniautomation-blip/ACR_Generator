import streamlit as st
from datetime import date
from db.sqlite_manager import SQLiteManager
from core.ai_engine import AIEngine
from core.afa_generator import AFAGenerator

def render():
    st.subheader("⚙️ Nuevo Análisis de Falla (AFA / FMEA)")
    
    with st.form("afa_form"):
        title = st.text_input("Título del Análisis de Falla")
        event_date = st.date_input("Fecha", value=date.today())
        area = st.selectbox("Área", ["Mantenimiento", "Operaciones", "Procesos", "Calidad", "Confiabilidad"])
        linea = st.text_input("Línea / Sistema")
        equipment = st.text_input("Equipo / Componente")
        criticality = st.selectbox("Criticidad", ["Alta", "Media", "Baja"])
        description = st.text_area("Descripción del Modo de Falla")
        
        submitted = st.form_submit_button("Generar AFA con IA")

        if submitted:
            if not title or not description:
                st.error("Complete título y descripción.")
            else:
                db = SQLiteManager()
                ai = AIEngine(provider="Gemini Flash")
                afa_gen = AFAGenerator(db, ai)
                with st.spinner("Ejecutando AFA..."):
                    event_id = afa_gen.process_afa(
                        title=title, event_date=str(event_date), area=area,
                        linea=linea, equipment=equipment, criticality=criticality,
                        description=description, username=st.session_state.get("username", "admin")
                    )
                st.success(f"¡AFA generado con éxito! ID de Evento: #{event_id}")

