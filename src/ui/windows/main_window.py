""" src/ui/main_window.py """

from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from src.ui.windows.file_text_prediction import FileTextPredictionWindow
from src.ui.windows.live_text_prediction import LiveTextPredictionWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Language predictor")
        
        central_widget = QWidget()
        layout = QVBoxLayout()
        
        label = QLabel("How would you like to predict texts?")
        layout.addWidget(label)
        
        live_text_button = QPushButton("Live text prediction")
        live_text_button.clicked.connect(self.open_live_text_prediction_window)  # Connect button to method
        file_text_button = QPushButton("File text prediction")
        file_text_button.clicked.connect(self.open_file_text_prediction_window)  # Connect button to method
        layout.addWidget(live_text_button)
        layout.addWidget(file_text_button)
        
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_file_text_prediction_window(self):
        self.file_text_window = FileTextPredictionWindow()
        self.file_text_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)  # Clean up on close
        self.file_text_window.show()

    def open_live_text_prediction_window(self):
        self.live_text_window = LiveTextPredictionWindow()
        self.live_text_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)  # Clean up on close
        self.live_text_window.show()
