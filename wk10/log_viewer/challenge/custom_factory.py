from interfaces.data_source import ILogSource
from services.file_source import FileLogSource
from services.mock_source import MockLogSource
# Import คลาสใหม่ที่เราเพิ่งสร้าง
from challenge.csv_source import CsvLogSource

class ChallengeSourceFactory:
    @staticmethod
    def create(source_type: str, path: str = None) -> ILogSource:
        if source_type == "file":
            return FileLogSource(path)
        elif source_type == "mock":
            return MockLogSource()
        elif source_type == "csv":
            # ส่งคืน Instance ของ CsvLogSource
            return CsvLogSource(path)
        else:
            raise ValueError("Unknown source type")