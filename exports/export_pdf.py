import html
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from core.report_generator import ReportGenerator

class PDFExporter:
    """Generador oficial de reportes PDF bajo el estándar MAN-F-054 (ACR & AFA)."""

    def __init__(self, report_gen: ReportGenerator):
        self.report_gen = report_gen

    def _safe(self, text: str) -> str:
        """Función auxiliar para escapar de forma segura caracteres HTML/XML para ReportLab."""
        if not text:
            return ""
        return html.escape(str(text))

    def generate(self, event_id: int, output_path: str) -> str:
        data = self.report_gen.get_event_data(event_id)
        event = data["event"]
        acr = data["acr"]
        afa = data["afa"]
        actions = data["actions"]
        doc_data = acr if acr else afa

        doc = SimpleDocTemplate(output_path, pagesize=letter, rightMargin=25, leftMargin=25, topMargin=25, bottomMargin=25)
        elements = []
        styles = getSampleStyleSheet()

        title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=13, textColor=colors.HexColor("#0F2C59"), spaceAfter=4, alignment=1)
        subtitle_style = ParagraphStyle('SubTitleStyle', parent=styles['Heading2'], fontSize=9, textColor=colors.HexColor("#1E3A8A"), spaceBefore=6, spaceAfter=3)
        normal_style = ParagraphStyle('NormalStyle', parent=styles['Normal'], fontSize=7.5, textColor=colors.HexColor("#1E293B"))
        bold_style = ParagraphStyle('BoldStyle', parent=normal_style, fontName="Helvetica-Bold")

        elements.append(Paragraph("ESTÁNDAR MAN-F-054: ANÁLISIS DE CAUSA RAÍZ & FALLAS (ACR / AFA)", title_style))
        elements.append(Spacer(1, 2))

        # 1. Datos Generales y Cabecera Oficial MAN-F-054
        header_data = [
            [Paragraph("<b>Título del Evento:</b>", bold_style), Paragraph(self._safe(event.get('title', '')), normal_style),
             Paragraph("<b>Fecha:</b>", bold_style), Paragraph(self._safe(event.get('event_date', '')), normal_style)],
            [Paragraph("<b>Área:</b>", bold_style), Paragraph(self._safe(event.get('area', '')), normal_style),
             Paragraph("<b>Línea / Planta:</b>", bold_style), Paragraph(self._safe(event.get('linea', '')), normal_style)],
            [Paragraph("<b>Equipo / Tag:</b>", bold_style), Paragraph(self._safe(event.get('equipment', '')), normal_style),
             Paragraph("<b>Criticidad:</b>", bold_style), Paragraph(self._safe(event.get('criticality', '')), normal_style)],
            [Paragraph("<b>Líder de Análisis:</b>", bold_style), Paragraph(self._safe(doc_data.get('leader', 'N/A')), normal_style),
             Paragraph("<b>Participantes:</b>", bold_style), Paragraph(self._safe(doc_data.get('participants', 'N/A')), normal_style)]
        ]
        t_header = Table(header_data, colWidths=[90, 200, 80, 192])
        t_header.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
            ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ]))
        elements.append(t_header)
        elements.append(Spacer(1, 4))

        # 2. Descripción del Problema (5W + 2H)
        elements.append(Paragraph("1. Descripción del Problema y Enfoque 5W+2H", subtitle_style))
        prob_data = [
            [Paragraph("<b>Problema Enfocado:</b>", bold_style), Paragraph(self._safe(doc_data.get('problem_definition', '')), normal_style)],
            [Paragraph("<b>¿Qué pasó? (Contexto):</b>", bold_style), Paragraph(self._safe(doc_data.get('what_happened', '')), normal_style)],
            [Paragraph("<b>¿Cómo ocurrió?:</b>", bold_style), Paragraph(self._safe(doc_data.get('how_happened', '')), normal_style)],
            [Paragraph("<b>¿Quién detectó?:</b>", bold_style), Paragraph(self._safe(doc_data.get('who_detected', '')), normal_style)],
            [Paragraph("<b>¿Cuánto (Pérdida/Impacto)?:</b>", bold_style), Paragraph(self._safe(doc_data.get('how_much_loss', '')), normal_style)],
            [Paragraph("<b>¿Cuál material/componente?:</b>", bold_style), Paragraph(self._safe(doc_data.get('which_materials', '')), normal_style)],
            [Paragraph("<b>¿Dónde / Cuándo inició?:</b>", bold_style), Paragraph(f"Lugar: {self._safe(doc_data.get('where_located', ''))} | Inicio: {self._safe(doc_data.get('when_started', ''))}", normal_style)],
            [Paragraph("<b>Acción Inmediata (Contención):</b>", bold_style), Paragraph(self._safe(doc_data.get('immediate_action', '')), normal_style)]
        ]
        t_prob = Table(prob_data, colWidths=[130, 432])
        t_prob.setStyle(TableStyle([
            ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
            ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#F1F5F9")),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ]))
        elements.append(t_prob)
        elements.append(Spacer(1, 4))

        # 3. Análisis de los 5 Porqués
        elements.append(Paragraph("2. Análisis de los 5 Porqués (Metodología Causa Raíz)", subtitle_style))
        whys_data = [
            [Paragraph("<b>Nivel</b>", bold_style), Paragraph("<b>Descripción del Análisis Técnico</b>", bold_style)],
            [Paragraph("¿Por qué 1?", bold_style), Paragraph(self._safe(doc_data.get('why_1', 'N/A')), normal_style)],
            [Paragraph("¿Por qué 2?", bold_style), Paragraph(self._safe(doc_data.get('why_2', 'N/A')), normal_style)],
            [Paragraph("¿Por qué 3?", bold_style), Paragraph(self._safe(doc_data.get('why_3', 'N/A')), normal_style)],
            [Paragraph("¿Por qué 4?", bold_style), Paragraph(self._safe(doc_data.get('why_4', 'N/A')), normal_style)],
            [Paragraph("¿Por qué 5 (Raíz)", bold_style), Paragraph(self._safe(doc_data.get('why_5', 'N/A')), normal_style)]
        ]
        t_whys = Table(whys_data, colWidths=[80, 482])
        t_whys.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0F2C59")),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ]))
        elements.append(t_whys)
        elements.append(Spacer(1, 4))

        # 4. Conclusiones y Causas
        elements.append(Paragraph("3. Conclusiones y Determinación de Causas", subtitle_style))
        causes_data = [
            [Paragraph("<b>Causa Física / Directa:</b>", bold_style), Paragraph(self._safe(doc_data.get('physical_cause', 'N/A')), normal_style)],
            [Paragraph("<b>Causa Contribuyente:</b>", bold_style), Paragraph(self._safe(doc_data.get('contributor_cause', 'N/A')), normal_style)],
            [Paragraph("<b>Causa Raíz Sistémica:</b>", bold_style), Paragraph(self._safe(doc_data.get('root_cause', 'N/A')), normal_style)]
        ]
        t_causes = Table(causes_data, colWidths=[130, 432])
        t_causes.setStyle(TableStyle([
            ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
            ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#F1F5F9")),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ]))
        elements.append(t_causes)
        elements.append(Spacer(1, 4))

        # 5. Plan de Acción y Seguimiento MAN-F-054
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
                Paragraph(self._safe(act.get('action_text', '')), normal_style),
                Paragraph(self._safe(act.get('objective', '')), normal_style),
                Paragraph(self._safe(act.get('responsible', '')), normal_style),
                Paragraph(self._safe(act.get('priority', '')), normal_style),
                Paragraph(self._safe(act.get('due_date', '')), normal_style),
                Paragraph(self._safe(act.get('status', '')), normal_style)
            ])

        t_actions = Table(action_table_data, colWidths=[150, 120, 90, 50, 70, 82])
        t_actions.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#0F2C59")),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ]))
        elements.append(t_actions)

        doc.build(elements)
        return output_path
