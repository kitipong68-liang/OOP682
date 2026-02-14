import csv
from typing import List
# อ้างอิง Interface เดิมจากโปรเจกต์หลัก
from interfaces.data_source import ILogSource

class CsvLogSource(ILogSource):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def get_logs(self) -> List[str]:
        logs = []
        try:
            # อ่านไฟล์ CSV
            with open(self.filepath, mode='r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    # แปลงแต่ละ Row ให้เป็น String (คั่นด้วย | )
                    # เพื่อให้ตรงกับ format ที่ UI คาดหวัง (List[str])
                    formatted_line = " | ".join(row)
                    logs.append(formatted_line)
            return logs
        except FileNotFoundError:
            return ["Error: CSV file not found."]
        except Exception as e:
            return [f"Error reading CSV: {str(e)}"]