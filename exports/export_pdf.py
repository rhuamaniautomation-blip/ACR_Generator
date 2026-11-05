from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from core.report_generator import ReportGenerator

class PDFExporter:
    """Generador de reportes en PDF."""

    def __init__(self, report_gen: ReportGenerator):
        self.report_gen = report_gen

    def generate(self, event_id: int, output_path: str) -> str:
        data = self.report_gen.get_event_data(event_id)
        event = data["event"]
        acr = data["acr"]
        actions = data["actions"]

        doc = SimpleDocTemplate(output_path, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
        elements = []
        styles = getSampleStyleSheet()

        title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=16, textColor=colors.HexColor("#1A365D"), spaceAfter=10)
        heading_style = ParagraphStyle('HeadingStyle', parent=styles['Heading2'], fontSize=11, textColor=colors.HexColor("#2B6CB0"), spaceBefore=8, spaceAfter=4)
        normal_style = styles['Normal']

        elements.append(Paragraph("REPORTE OFICIAL DE ANÁLISIS DE CAUSA RAÍZ (ACR)", title_style))
        elements.append(Paragraph(f"<b>Título:</b> {event.get('title', '')} | <b>Fecha:</b> {event.get('event_date', '')}", normal_style))
        elements.append(Paragraph(f"<b>Área:</b> {event.get('area', '')} | <b>Línea:</b> {event.get('linea', '')} | <b>Equipo:</b> {event.get('equipment', '')}", normal_style))
        elements.append(Spacer(1, 8))

        elements.append(Paragraph("1. Definición del Problema", heading_style))
        elements.append(Paragraph(acr.get('problem_definition', 'N/A'), normal_style))

        elements.append(Paragraph("2. Análisis de los 5 Porqués", heading_style))
        for w in ['why_1', 'why_2', 'why_3', 'why_4', 'why_5']:
            elements.append(Paragraph(f"<b>{w.upper()}:</b> {acr.get(w, '')}", normal_style))

        elements.append(Paragraph("3. Conclusiones", heading_style))
        elements.append(Paragraph(f"<b>Causa Física:</b> {acr.get('physical_cause', '')}", normal_style))
        elements.append(Paragraph(f"<b>Causa Raíz:</b> {acr.get('root_cause', '')}", normal_style))

        elements.append(Paragraph("4. Plan de Acción", heading_style))
        table_data = [["Acción", "Objetivo", "Responsable", "Prioridad", "Fecha", "Estado"]]
        for act in actions:
            table_data.append([act.get('action_text', ''), act.get('objective', ''), act.get('responsible', ''), act.get('priority', ''), act.get('due_date', ''), act.get('status', '')])

        t = Table(table_data, colWidths=[120, 100, 80, 50, 65, 65])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2B6CB0")),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
        ]))
        elements.append(t)

        doc.build(elements)
        return output_path

