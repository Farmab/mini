import sys
import os
from PySide6.QtWidgets import QApplication
from database.db_manager import DatabaseManager
from ui.login import LoginWindow
from ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    
    # Initialize database
    db = DatabaseManager()
    db.init_db()
    db.create_admin_user()
    
    # Create and show login window
    login_window = LoginWindow()
    main_window = MainWindow()
    
    # Connect login success signal
    login_window.login_successful.connect(lambda user_data: (
        main_window.set_user(user_data),
        main_window.show(),
        login_window.hide()
    ))
    
    login_window.show()
    return app.exec()

if __name__ == '__main__':
    main()
