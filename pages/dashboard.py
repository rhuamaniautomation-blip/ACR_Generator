import streamlit as st
import pandas as pd
import plotly.express as px
from db.sqlite_manager import SQLiteManager

def render():
    st.subheader("📊 Dashboard Ejecutivo de Confiabilidad y ACR / AFA")
    db = SQLiteManager()

    events = db.execute_query("SELECT * FROM events")
    acr_count = len(db.execute_query("SELECT * FROM acr"))
    afa_count = len(db.execute_query("SELECT * FROM afa"))
    actions = db.execute_query("SELECT * FROM actions")

    total_events = len(events)
    open_actions = len([a for a in actions if a["status"] == "Pendiente"])
    overdue_actions = len([a for a in actions if a["status"] == "Vencida"])
    closed_actions = len([a for a in actions if a["status"] == "Completada"])

    c1, c2, c3, c4, c5, c6 = st.columns(6)
    c1.metric("Eventos", total_events)
    c2.metric("ACR", acr_count)
    c3.metric("AFA", afa_count)
    c4.metric("Abiertas", open_actions)
    c5.metric("Vencidas", overdue_actions)
    c6.metric("Cerradas", closed_actions)

    st.markdown("---")
    if total_events > 0:
        df_events = pd.DataFrame([dict(e) for e in events])
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("### Eventos por Área")
            fig_area = px.pie(df_events, names='area', hole=0.4)
            st.plotly_chart(fig_area, use_container_width=True)
        with col_b:
            st.markdown("### Eventos por Criticidad")
            fig_crit = px.bar(df_events, x='criticality', color='criticality')
            st.plotly_chart(fig_crit, use_container_width=True)
    else:
        st.info("No hay eventos registrados.")

