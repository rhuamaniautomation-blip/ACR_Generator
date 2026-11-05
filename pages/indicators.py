import streamlit as st
import pandas as pd
import plotly.express as px
from db.sqlite_manager import SQLiteManager

def render():
    st.subheader("📈 Indicadores Clave de Confiabilidad")
    db = SQLiteManager()
    actions = db.execute_query("SELECT * FROM actions")
    if actions:
        df = pd.DataFrame([dict(a) for a in actions])
        fig = px.bar(df['status'].value_counts().reset_index(), x='status', y='count', color='status')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Sin datos para indicadores.")

    c1, c2, c3 = st.columns(3)
    c1.metric("MTBF Promedio", "742 Horas")
    c2.metric("MTTR Promedio", "3.4 Horas")
    c3.metric("Disponibilidad", "98.5%")

