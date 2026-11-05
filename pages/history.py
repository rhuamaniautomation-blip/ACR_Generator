import streamlit as st
import pandas as pd
from db.sqlite_manager import SQLiteManager
from core.report_generator import ReportGenerator
from exports.export_pdf import PDFExporter
from exports.export_word import WordExporter
from exports.export_excel import ExcelExporter

def render():
    st.subheader("📂 Historial de Eventos, ACR y AFA")
    db = SQLiteManager()
    events = db.execute_query("SELECT * FROM events ORDER BY id DESC")

    if not events:
        st.info("No hay eventos registrados.")
        return

    df = pd.DataFrame([dict(e) for e in events])
    st.dataframe(df, use_container_width=True)

    selected_id = st.selectbox("Seleccione ID de Evento para Exportar", df['id'].tolist())
    if selected_id:
        report_gen = ReportGenerator(db)
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("📄 PDF"):
                path = f"evento_{selected_id}.pdf"
                PDFExporter(report_gen).generate(selected_id, path)
                with open(path, "rb") as f:
                    st.download_button("Descargar PDF", f, file_name=path)
        with c2:
            if st.button("📝 Word"):
                path = f"evento_{selected_id}.docx"
                WordExporter(report_gen).generate(selected_id, path)
                with open(path, "rb") as f:
                    st.download_button("Descargar Word", f, file_name=path)
        with c3:
            if st.button("📊 Excel"):
                path = f"evento_{selected_id}.xlsx"
                ExcelExporter(report_gen).generate(selected_id, path)
                with open(path, "rb") as f:
                    st.download_button("Descargar Excel", f, file_name=path)

