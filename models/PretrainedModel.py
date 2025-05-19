from tensorflow.keras.layers import Input, Dense, Dropout, GlobalAveragePooling2D
from tensorflow.keras.models import Model


class PretrainedModel:
    def __init__(self, image_size, num_classes, base_model):
        self.image_size = image_size
        self.input_shape = image_size + (3,)
        self.num_classes = num_classes
        
        # Create a Sequential model
        self.model = Sequential()
        
        # Add the base model (InceptionV3) without the top layers
        base_model_instance = base_model(weights=None, include_top=False, input_shape=self.input_shape)
        
        # Freeze the base model layers
        for layer in base_model_instance.layers:
            layer.trainable = False
        
        # Add layers to the Sequential model
        self.model.add(base_model_instance)
        self.model.add(GlobalAveragePooling2D())
        self.model.add(Dense(256, activation='relu', name='new_dense_1'))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(128, activation='relu', name='new_dense_2'))
        self.model.add(Dense(self.num_classes, activation='softmax', name='new_output'))

    def compile(self, optimizer, loss, metrics):
        self.model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

    def summary(self):
        self.model.summary()

    def call(self, inputs):
        return self.model(inputs)
       
    def load_model(