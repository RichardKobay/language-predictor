from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QLabel
)
from PyQt6.QtCore import QTimer
from src.utils.predictor import Predictor

class LiveTextPredictionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.predictor = Predictor()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Live Text Prediction")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)

        # Label to display the predicted language
        self.language_label = QLabel("Predicted Language: ")
        self.layout.addWidget(self.language_label)

        # Text area for user input
        self.text_area = QTextEdit()
        self.text_area.textChanged.connect(self.on_text_changed)
        self.layout.addWidget(self.text_area)

        self.setCentralWidget(self.central_widget)

        # Timer to handle inactivity
        self.inactivity_timer = QTimer()
        self.inactivity_timer.setInterval(2000)  # 2 seconds
        self.inactivity_timer.setSingleShot(True)
        self.inactivity_timer.timeout.connect(self.predict_language)

    def on_text_changed(self):
        """ Reset the timer whenever the text changes. """
        self.inactivity_timer.start()

    def predict_language(self):
        """ Predict the language of the text in the text area. """
        text = self.text_area.toPlainText()
        if text.strip():  # Only predict if there's text
            try:
                language = self.predictor.predict(text)
                self.language_label.setText(f"Predicted Language: {language}")
            except Exception as e:
                self.language_label.setText(f"Error: {str(e)}")
        else:
            self.language_label.setText("Predicted Language: ")

if __name__ == "__main__":
    app = QApplication([])
    window = LiveTextPredictionWindow()
    window.show()
    app.exec()
