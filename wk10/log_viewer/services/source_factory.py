# log_viewer/services/source_factory.py
from typing import Optional
from log_viewer.interfaces.data_source import ILogSource
from log_viewer.services.file_source import FileLogSource
from log_viewer.services.mock_source import MockLogSource
from log_viewer.services.csv_source import CsvLogSource

class SourceFactory:
    @staticmethod
    def create_source(source_type: str, filepath: Optional[str] = None) -> ILogSource:
        if source_type == "file":
            path = filepath or "logs/app.log"
            return FileLogSource(path)
        if source_type == "mock":
            return MockLogSource()
        if source_type == "csv":
            path = filepath or "logs/app.csv"
            return CsvLogSource(path)
        raise ValueError(f"Unknown source type: {source_type}")