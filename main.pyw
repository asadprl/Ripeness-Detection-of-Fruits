import sys
from PyQt6 import QtWidgets
from database import Database
from screens.login_screen import LoginScreen

def main():
    db = Database()
    app = QtWidgets.QApplication(sys.argv)
    login_screen = LoginScreen(db)
    login_screen.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
