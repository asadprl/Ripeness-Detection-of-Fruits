import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class RipenessClassifier:
    """Class to load a Keras model and classify images"""
    
    def __init__(self, config):
        """Initialize the Ripeness Classifier with the path to the model"""
        self.config = config
        self.model = load_model(config.model_path)
        
    def predict(self, img_path):
        """Predict the class of the image at img_path"""
        # Load the image
        img = image.load_img(img_path, target_size=self.config.image_size)  # Adjust target size as needed
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array /= 255.0  # Normalize the image

        # Make prediction
        predictions = self.model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)[0]  # Get the index of the highest probability

        return predicted_class
