from PySide6.QtWidgets import (QWidget, QVBoxLayout, QLineEdit,
                             QPushButton, QLabel, QFrame)
from PySide6.QtCore import Signal
from database.db_manager import DatabaseManager

class LoginWindow(QWidget):
    login_successful = Signal(dict)

    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('POS System Login')
        self.setFixedSize(400, 300)
        
        layout = QVBoxLayout()
        
        # Create a frame for the login form
        form_frame = QFrame()
        form_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                padding: 20px;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton {
                padding: 10px;
                background-color: #2ecc71;
                color: white;
                border: none;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        
        form_layout = QVBoxLayout(form_frame)
        
        # Title
        title = QLabel('Login to POS System')
        title.setStyleSheet('font-size: 20px; font-weight: bold; margin-bottom: 20px;')
        form_layout.addWidget(title)
        
        # Username input
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('Username')
        form_layout.addWidget(self.username_input)
        
        # Password input
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('Password')
        self.password_input.setEchoMode(QLineEdit.Password)
        form_layout.addWidget(self.password_input)
        
        # Error label
        self.error_label = QLabel('')
        self.error_label.setStyleSheet('color: red;')
        form_layout.addWidget(self.error_label)
        
        # Login button
        login_button = QPushButton('Login')
        login_button.clicked.connect(self.handle_login)
        form_layout.addWidget(login_button)
        
        layout.addWidget(form_frame)
        self.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        if not username or not password:
            self.error_label.setText('Please enter both username and password')
            return
        
        user_data = self.db.verify_login(username, password)
        if user_data:
            self.login_successful.emit(user_data)
        else:
            self.error_label.setText('Invalid username or password')
