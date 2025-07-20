from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QStackedWidget, QLabel)
from PySide6.QtCore import Qt
from ui.components.product_management import ProductManagement

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('POS System')
        self.setMinimumSize(1200, 800)

        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout(central_widget)

        # Create sidebar
        sidebar = QWidget()
        sidebar.setFixedWidth(200)
        sidebar.setStyleSheet("""
            QWidget {
                background-color: #2c3e50;
                color: white;
            }
            QPushButton {
                text-align: left;
                padding: 10px;
                border: none;
                color: white;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #34495e;
            }
        """)
        sidebar_layout = QVBoxLayout(sidebar)

        # Create menu buttons
        self.create_menu_button('Point of Sale', sidebar_layout)
        self.create_menu_button('Inventory', sidebar_layout, lambda: self.content_stack.setCurrentWidget(self.product_management))
        self.create_menu_button('Reports', sidebar_layout)
        self.create_menu_button('Settings', sidebar_layout)

        # Add stretch to push buttons to top
        sidebar_layout.addStretch()

        # Create user info section
        self.user_label = QLabel()
        self.user_label.setStyleSheet('padding: 10px; border-top: 1px solid #34495e;')
        sidebar_layout.addWidget(self.user_label)

        # Create stacked widget for content
        self.content_stack = QStackedWidget()
        self.content_stack.setStyleSheet('background-color: #f5f6fa;')

        # Create and add pages
        self.product_management = ProductManagement()
        self.content_stack.addWidget(self.product_management)

        # Add widgets to main layout
        layout.addWidget(sidebar)
        layout.addWidget(self.content_stack)

    def create_menu_button(self, text, layout, connection=None):
        button = QPushButton(text)
        if connection:
            button.clicked.connect(connection)
        layout.addWidget(button)

    def set_user(self, user_data):
        self.user_data = user_data
        self.user_label.setText(f'User: {user_data["username"]}\nRole: {user_data["role"]}')
