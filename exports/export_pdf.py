from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from core.report_generator import ReportGenerator

class PDFExporter:
    """Generador de reportes profesionales bajo formato MAN-F-054."""

    def __init__(self, report_gen: ReportGenerator):
        self.report_gen = report_gen

    def generate(self, event_id: int, output_path: str) -> str:
        data = self.report_gen.get_event_data(event_id)
        event = data["event"]
        acr = data["acr"]
        afa = data["afa"]
        actions = data["actions"]

        doc = SimpleDocTemplate(output_path, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
        elements = []
        styles = getSampleStyleSheet()

        title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=15, textColor=colors.HexColor("#1A365D"), spaceAfter=8, alignment=1)
        subtitle_style = ParagraphStyle('SubTitleStyle', parent=styles['Heading2'], fontSize=11, textColor=colors.HexColor("#2B6CB0"), spaceBefore=6, spaceAfter=4)
        normal_style = ParagraphStyle('NormalStyle', parent=styles['Normal'], fontSize=9, textColor=colors.HexColor("#2D3748"))
        bold_style = ParagraphStyle('BoldStyle', parent=normal_style, fontName="Helvetica-Bold")

        elements.append(Paragraph("ESTÁNDAR MAN-F-054: ANÁLISIS DE CAUSA RAÍZ & FALLAS (ACR / AFA)", title_style))
        elements.append(Spacer(1, 5))

        header_data = [
            [Paragraph("<b>Título del Evento:</b>", normal_style), Paragraph(event.get('title', ''), normal_style),
             Paragraph("<b>Fecha:</b>", normal_style), Paragraph(event.get('event_date', ''), normal_style)],
            [Paragraph("<b>Área:</b>", normal_style), Paragraph(event.get('area', ''), normal_style),
             Paragraph("<b>Línea / Planta:</b>", normal_style), Paragraph(event.get('linea', ''), normal_style)],
            [Paragraph("<b>Equipo / Tag:</b>", normal_style), Paragraph(event.get('equipment', ''), normal_style),
             Paragraph("<b>Criticidad:</b>", normal_style), Paragraph(event.get('criticality', ''), normal_style)]
        ]
        t_header = Table(header_data, colWidths=[90, 180, 80, 180])
        t_header.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F7FAFC")),
            ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ]))
        elements.append(t_header)
        elements.append(Spacer(1, 10))

        elements.append(Paragraph("1. Descripción del Problema (Enfoque 5W + 2H)", subtitle_style))
        prob_text = acr.get('problem_definition', '') or afa.get('effect', '') or event.get('description', 'N/A')
        elements.append(Paragraph(prob_text, normal_style))
        elements.append(Spacer(1, 8))

        elements.append(Paragraph("2. Análisis de los 5 Porqués (Metodología Causa Raíz)", subtitle_style))
        whys_data = [
            [Paragraph("<b>Nivel</b>", bold_style), Paragraph("<b>Descripción del Análisis</b>", bold_style)],
            [Paragraph("¿Por qué 1?", bold_style), Paragraph(acr.get('why_1', '') or afa.get('why_1', 'N/A'), normal_style)],
            [Paragraph("¿Por qué 2?", bold_style), Paragraph(acr.get('why_2', '') or afa.get('why_2', 'N/A'), normal_style)],
            [Paragraph("¿Por qué 3?", bold_style), Paragraph(acr.get('why_3', '') or afa.get('why_3', 'N/A'), normal_style)],
            [Paragraph("¿Por qué 4?", bold_style), Paragraph(acr.get('why_4', '') or afa.get('why_4', 'N/A'), normal_style)],
            [Paragraph("¿Por qué 5 (Raíz)", bold_style), Paragraph(acr.get('why_5', '') or afa.get('why_5', 'N/A'), normal_style)]
        ]
        t_whys = Table(whys_data, colWidths=[90, 440])
        t_whys.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2B6CB0")),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ]))
        elements.append(t_whys)
        elements.append(Spacer(1, 10))

        elements.append(Paragraph("3. Conclusiones y Determinación de Causas", subtitle_style))
        causes_data = [
            [Paragraph("<b>Causa Física / Directa:</b>", bold_style), Paragraph(acr.get('physical_cause', '') or afa.get('failure_mode', 'N/A'), normal_style)],
            [Paragraph("<b>Causa Contribuyente:</b>", bold_style), Paragraph(acr.get('contributor_cause', '') or afa.get('consequence', 'N/A'), normal_style)],
            [Paragraph("<b>Causa Raíz Sistémica:</b>", bold_style), Paragraph(acr.get('root_cause', '') or afa.get('root_cause', 'N/A'), normal_style)]
        ]
        t_causes = Table(causes_data, colWidths=[140, 390])
        t_causes.setStyle(TableStyle([
            ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
            ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#EDF2F7")),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ]))
        elements.append(t_causes)
        elements.append(Spacer(1, 10))

        elements.append(Paragraph("4. Plan de Acción y Seguimiento", subtitle_style))
        action_table_data = [[
            Paragraph("<b>Acción</b>", bold_style),
            Paragraph("<b>Objetivo</b>", bold_style),
            Paragraph("<b>Responsable</b>", bold_style),
            Paragraph("<b>Prioridad</b>", bold_style),
            Paragraph("<b>Fecha</b>", bold_style),
            Paragraph("<b>Estado</b>", bold_style)
        ]]
        for act in actions:
            action_table_data.append([
                Paragraph(act.get('action_text', ''), normal_style),
                Paragraph(act.get('objective', ''), normal_style),
                Paragraph(act.get('responsible', ''), normal_style),
                Paragraph(act.get('priority', ''), normal_style),
                Paragraph(act.get('due_date', ''), normal_style),
                Paragraph(act.get('status', ''), normal_style)
            ])

        t_actions = Table(action_table_data, colWidths=[150, 110, 80, 55, 65, 70])
        t_actions.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2B6CB0")),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ]))
        elements.append(t_actions)

        doc.build(elements)
        return output_path
