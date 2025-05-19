"""
User authentication screen implementation
"""


from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMessageBox
from screens.main_screen import MainScreen
from database import Database

class LoginScreen(QtWidgets.QMainWindow):
    """Login window handling user authentication"""
    
    def __init__(self, db, config):
        super(LoginScreen, self).__init__()
        
        self.config = config
        
        # Load UI design from file
        uic.loadUi(config.ui_login, self)
        
        # Initialize database connection
        self.db = db
        
        # Connect button click events to handlers
        self.btn_login.clicked.connect(self.login)

    def login(self):
        """Handle login button click event"""
        
        # Get user input
        username = self.edit_username.text()
        password = self.edit_password.text()
        
        # Verify credentials
        if self.db.authenticate_user(username, password):
            # Successful login - open main screen
            self.main_screen = MainScreen(self.config)
            self.main_screen.show()
            self.close()
        else:
            # Failed login - show error
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
