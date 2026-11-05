import pandas as pd
from core.report_generator import ReportGenerator

class ExcelExporter:
    """Generador de reportes en Excel."""

    def __init__(self, report_gen: ReportGenerator):
        self.report_gen = report_gen

    def generate(self, event_id: int, output_path: str) -> str:
        data = self.report_gen.get_event_data(event_id)
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            pd.DataFrame([data["event"]]).to_excel(writer, sheet_name='Evento', index=False)
            pd.DataFrame([data["acr"]]).to_excel(writer, sheet_name='ACR', index=False)
            pd.DataFrame(data["actions"]).to_excel(writer, sheet_name='Acciones', index=False)
        return output_path
