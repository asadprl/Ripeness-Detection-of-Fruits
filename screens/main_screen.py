from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from PyQt6.QtGui import QPixmap
import random

class MainScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        uic.loadUi('ui/main.ui', self)
        self.upload_button.clicked.connect(self.upload_image)
        self.classify_button.clicked.connect(self.classify_image)
        self.image_path = ""

    def upload_image(self):
        options = QFileDialog.Options()
        self.image_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.xpm *.jpg *.jpeg);;All Files (*)", options=options)
        if self.image_path:
            pixmap = QPixmap(self.image_path)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), aspectRatioMode=True))

    def classify_image(self):
        if not self.image_path:
            QMessageBox.warning(self, "No Image", "Please upload an image first.")
            return
        
        # Dummy classification logic
        classification = random.choice(["Unripe", "Ripe", "Overripe"])
        
        if classification == "Unripe":
            color = "red"
        elif classification == "Ripe":
            color = "green"
        else:
            color = "yellow"
        
        self.classification_label.setText(classification)
        self.classification_label.setStyleSheet(f"color: {color};")