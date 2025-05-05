"""
Main application screen for image classification functionality
"""

from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from PyQt6.QtGui import QPixmap
import random


class MainScreen(QtWidgets.QMainWindow):
    """Main application window with image classification features"""
    
    def __init__(self):
        super(MainScreen, self).__init__()
        
        # Load UI design from file
        uic.loadUi('ui/mainwindow.ui', self)
        
        # Connect button click events to handlers
        self.btn_upload.clicked.connect(self.upload_image)
        self.btn_classify.clicked.connect(self.classify_image)
        
        # Initialize image path variable
        self.image_path = ""

    def upload_image(self):
        """Handle image selection and display"""
        
        # Open file dialog to select image
        self.image_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg);;All Files (*)")
        if self.image_path:
            # Load and display selected image
            pixmap = QPixmap(self.image_path)
            print(self.lbl_image.size())
            scaled_pixmap = pixmap.scaled(self.lbl_image.size())
            self.lbl_image.setPixmap(scaled_pixmap)

    def classify_image(self):
        """Handle image classification (mock implementation)"""
        
        if not self.image_path:
            QMessageBox.warning(self, "No Image", "Please upload an image first.")
            return
        
        # Temporary random classification for demonstration
        classification = random.choice(["Unripe", "Ripe", "Overripe"])
        
        # Set result styling based on classification
        color = "yellow" if classification == "Unripe" else \
               "green" if classification == "Ripe" else \
               "red"    # for overripe
        
        self.lbl_result.setText(classification)
        self.lbl_result.setStyleSheet(f"color: {color}; border: 2px solid {color}")

