import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget, QListWidget, QMessageBox
)
from src.utils.predictor import Predictor

class FileTextPredictionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.predictor = Predictor()
        self.initUI()
        
        
    def initUI(self):
        self.setWindowTitle("File Text Prediction")
        self.setGeometry(100, 100, 600, 400)
        
        self.central_widget = QWidget()
        
        self.layout = QVBoxLayout(self.central_widget)
        self.select_folder_button = QPushButton("Select Folder")
        self.select_folder_button.clicked.connect(self.select_folder)
        self.layout.addWidget(self.select_folder_button)

        self.file_list_widget = QListWidget()
        self.layout.addWidget(self.file_list_widget)

        self.setCentralWidget(self.central_widget)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.process_folder(folder_path)

    def process_folder(self, folder_path):
        self.file_list_widget.clear()
        try:
            for filename in os.listdir(folder_path):
                if filename.endswith(".txt"):
                    file_path = os.path.join(folder_path, filename)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        language = self.predictor.predict(content)
                        self.file_list_widget.addItem(f"{filename}: {language}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
