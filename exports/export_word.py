from docx import Document
from core.report_generator import ReportGenerator

class WordExporter:
    """Generador de reportes en Word."""

    def __init__(self, report_gen: ReportGenerator):
        self.report_gen = report_gen

    def generate(self, event_id: int, output_path: str) -> str:
        data = self.report_gen.get_event_data(event_id)
        event = data["event"]
        acr = data["acr"]
        actions = data["actions"]

        doc = Document()
        doc.add_heading("REPORTE OFICIAL DE ANÁLISIS DE CAUSA RAÍZ (ACR)", level=1)
        doc.add_paragraph(f"Título: {event.get('title', '')}")
        doc.add_paragraph(f"Área: {event.get('area', '')} | Equipo: {event.get('equipment', '')}")
        
        doc.add_heading("1. Definición del Problema", level=2)
        doc.add_paragraph(acr.get('problem_definition', ''))

        doc.add_heading("2. Los 5 Porqués", level=2)
        for w in ['why_1', 'why_2', 'why_3', 'why_4', 'why_5']:
            doc.add_paragraph(f"{w.upper()}: {acr.get(w, '')}")

        doc.add_heading("3. Plan de Acción", level=2)
        table = doc.add_table(rows=1, cols=6)
        hdr_cells = table.rows[0].cells
        for i, name in enumerate(["Acción", "Objetivo", "Responsable", "Prioridad", "Fecha", "Estado"]):
            hdr_cells[i].text = name

        for act in actions:
            row_cells = table.add_row().cells
            row_cells[0].text = act.get('action_text', '')
            row_cells[1].text = act.get('objective', '')
            row_cells[2].text = act.get('responsible', '')
            row_cells[3].text = act.get('priority', '')
            row_cells[4].text = act.get('due_date', '')
            row_cells[5].text = act.get('status', '')

        doc.save(output_path)
        return output_path

