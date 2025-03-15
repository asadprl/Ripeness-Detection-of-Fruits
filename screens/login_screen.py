from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
from database import Database

class LoginScreen(QtWidgets.QMainWindow):
    def __init__(self, db):
        super(LoginScreen, self).__init__()
        uic.loadUi('ui/login.ui', self)
        self.db = db  # Use the passed database instance
        self.login_button.clicked.connect(self.login)

    def login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        
        if self.db.authenticate_user(username, password):
            self.main_screen = MainScreen()
            self.main_screen.show()
            self.close()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")