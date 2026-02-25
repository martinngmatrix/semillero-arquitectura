from abc import ABC, abstractmethod

class ReportExporter(ABC):
    @abstractmethod
    def export(self, data: dict) -> None:
        pass

class PDFExporter(ReportExporter):
    def export(self, data: dict) -> None:
        print("Exportando reporte en PDF")


class CSVExporter(ReportExporter):
    def export(self, data: dict) -> None:
        print("Exportando reporte en CSV")

class ReportService(ABC):

    # Factory Method
    @abstractmethod
    def create_exporter(self) -> ReportExporter:
        pass

    def generate_report(self, data: dict) -> None:
        print("Validando datos...")
        exporter = self.create_exporter()
        exporter.export(data)
        print("Reporte generado.")

class SalesReportService(ReportService):
    def create_exporter(self) -> ReportExporter:
        return PDFExporter()


class AuditReportService(ReportService):
    def create_exporter(self) -> ReportExporter:
        return CSVExporter()

def client_code(service: ReportService):
    service.generate_report({"total": 1000})


if __name__ == "__main__":
    client_code(SalesReportService())
    client_code(AuditReportService())
