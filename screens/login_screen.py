from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
from screens.main_screen import MainScreen
from database import Database

class LoginScreen(QtWidgets.QMainWindow):
    def __init__(self, db):
        super(LoginScreen, self).__init__()
        uic.loadUi('ui/login.ui', self)
        self.db = db
        self.btn_login.setDefault(True)
        self.btn_login.clicked.connect(self.login)

    def login(self):
        username = self.edit_username.text()
        password = self.edit_password.text()
        
        if self.db.authenticate_user(username, password):
            self.main_screen = MainScreen()
            self.main_screen.show()
            self.close()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
