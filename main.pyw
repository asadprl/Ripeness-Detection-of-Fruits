"""
Main Application Entry Point for Fruit Ripeness Detection System
"""

import sys
from PyQt6 import QtWidgets
from database import Database
from screens.login_screen import LoginScreen

def main():
    """ Main function to initialize and start the application """
    
    # Initialize the database
    db = Database()
    
    # Create a Qt Application Instance
    app = QtWidgets.QApplication(sys.argv)
    
    # Create and show Login Screen
    login_screen = LoginScreen(db)
    login_screen.show()
    
    # Start the application event loop
    sys.exit(app.exec())


"""Entry point when executed directly"""
if __name__ == "__main__":
    main()
