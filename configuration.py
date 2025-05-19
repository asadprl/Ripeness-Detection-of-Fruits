class Configuration:
    def __init__(self):
        self.db_name = 'users.db'
        self.ui_login = 'ui/login.ui'
        self.ui_mainscreen = 'ui/mainwindow.ui'
        self.model_path = 'models/inceptionv3_model.h5'
        self.image_size = (224,224)
        self.num_classes = 3