from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from PyQt6.QtGui import QPixmap
import random


class MainScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        uic.loadUi('ui/mainwindow.ui', self)
        self.btn_upload.clicked.connect(self.upload_image)
        self.btn_classify.clicked.connect(self.classify_image)
        self.image_path = ""

    def upload_image(self):
        self.image_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg);;All Files (*)")
        if self.image_path:
            pixmap = QPixmap(self.image_path)
            print(self.lbl_image.size())
            scaled_pixmap = pixmap.scaled(self.lbl_image.size())
            self.lbl_image.setPixmap(scaled_pixmap)

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
        
        self.lbl_result.setText(classification)
        self.lbl_result.setStyleSheet(f"color: {color}; border: 2px solid {color}")

