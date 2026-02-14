import sys
import os

# เทคนิค: เพิ่ม Path เพื่อให้ Python มองเห็น modules ใน parent folder
# (จำเป็นเพราะเราย้าย main มาอยู่ใน subfolder)
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from challenge.custom_factory import ChallengeSourceFactory

def main():
    app = QApplication(sys.argv)

    # 1. ใช้ Factory สร้าง Source แบบ CSV
    # สังเกตว่าเราส่ง path ของไฟล์ csv เข้าไป
    source = ChallengeSourceFactory.create("csv", "challenge/data.csv")

    # 2. Inject source เข้าไปใน UI ตัวเดิม (Dependency Injection)
    # เราไม่ได้แก้โค้ด MainWindow เลยแม้แต่บรรทัดเดียว!
    window = MainWindow(source)
    
    window.setWindowTitle("Log Viewer (Challenge Mode - CSV)")
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()