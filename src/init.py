""" src/init.py """

import sys
from PyQt6.QtWidgets import QApplication
from src.ui.windows.main_window import MainWindow
from src.utils.config import AppConfig

def run() -> None:
    """
    Run the application.
    """
    app = QApplication(sys.argv)
    AppConfig.initialize()
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
