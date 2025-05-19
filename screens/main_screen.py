"""
Main application screen for image classification functionality
"""

from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from PyQt6.QtGui import QPixmap
from ripeness_classifier import RipenessClassifier


class MainScreen(QtWidgets.QMainWindow):
    """Main application window with image classification features"""
    
    def __init__(self, config):
        super(MainScreen, self).__init__()
        
        self.config = config
        
        # Load UI design from file
        uic.loadUi(config.ui_mainscreen, self)
        
        # Connect button click events to handlers
        self.btn_upload.clicked.connect(self.upload_image)
        self.btn_classify.clicked.connect(self.classify_image)
        
        # Initialize image path variable
        self.image_path = ""
        
        # Initialize the ripeness classifier
        self.ripeness_classifier = RipenessClassifier(config)


    def upload_image(self):
        """Handle image selection and display"""
        
        # Open file dialog to select image
        self.image_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg);;All Files (*)")
        if self.image_path:
            # Load and display selected image
            pixmap = QPixmap(self.image_path)
            scaled_pixmap = pixmap.scaled(self.lbl_image.size())
            self.lbl_image.setPixmap(scaled_pixmap)

    def classify_image(self):
        """Handle image classification using the loaded model"""
        
        if not self.image_path:
            QMessageBox.warning(self, "No Image", "Please upload an image first.")
            return
        
        # Use the model classifier to predict the class
        predicted_class = self.ripeness_classifier.predict(self.image_path)
        
        # Map the predicted class index to a label (update this mapping as per your model's classes)
        class_labels = {0: "Overripe", 1: "Ripe", 2: "Unripe"}
        classification = class_labels.get(predicted_class, "Unknown")
        
        # Set result styling based on classification
        color = "yellow" if classification == "Unripe" else \
               "green" if classification == "Ripe" else \
               "red"    # for Overripe
        
        self.lbl_result.setText(classification)
        self.lbl_result.setStyleSheet(f"color: {color}; border: 2px solid {color}")

