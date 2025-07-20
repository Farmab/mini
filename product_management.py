from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                             QTableWidget, QTableWidgetItem, QDialog, QLineEdit,
                             QFormLayout, QMessageBox, QLabel)
from PySide6.QtCore import Qt
from database.db_manager import DatabaseManager

class ProductDialog(QDialog):
    def __init__(self, parent=None, product_data=None):
        super().__init__(parent)
        self.product_data = product_data
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Add Product' if not self.product_data else 'Edit Product')
        layout = QFormLayout(self)

        # Create input fields
        self.name_input = QLineEdit(self.product_data['name'] if self.product_data else '')
        self.barcode_input = QLineEdit(self.product_data['barcode'] if self.product_data else '')
        self.price_input = QLineEdit(str(self.product_data['price']) if self.product_data else '')
        self.stock_input = QLineEdit(str(self.product_data['stock']) if self.product_data else '')
        self.category_input = QLineEdit(self.product_data['category'] if self.product_data else '')

        # Add fields to layout
        layout.addRow('Name:', self.name_input)
        layout.addRow('Barcode:', self.barcode_input)
        layout.addRow('Price:', self.price_input)
        layout.addRow('Stock:', self.stock_input)
        layout.addRow('Category:', self.category_input)

        # Add buttons
        button_layout = QHBoxLayout()
        save_button = QPushButton('Save')
        save_button.clicked.connect(self.accept)
        cancel_button = QPushButton('Cancel')
        cancel_button.clicked.connect(self.reject)

        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        layout.addRow('', button_layout)

    def get_product_data(self):
        return {
            'name': self.name_input.text(),
            'barcode': self.barcode_input.text(),
            'price': float(self.price_input.text()),
            'stock': int(self.stock_input.text()),
            'category': self.category_input.text()
        }

class ProductManagement(QWidget):
    def __init__(self):
        super().__init__()
        self.db = DatabaseManager()
        self.setup_ui()
        self.load_products()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        # Header
        header_layout = QHBoxLayout()
        title = QLabel('Product Management')
        title.setStyleSheet('font-size: 24px; font-weight: bold;')
        header_layout.addWidget(title)
        header_layout.addStretch()

        # Add Product button
        add_button = QPushButton('Add Product')
        add_button.setStyleSheet("""
            QPushButton {
                background-color: #2ecc71;
                color: white;
                padding: 8px 15px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #27ae60;
            }
        """)
        add_button.clicked.connect(self.add_product)
        header_layout.addWidget(add_button)
        layout.addLayout(header_layout)

        # Create table
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['ID', 'Name', 'Barcode', 'Price', 'Stock', 'Category', 'Actions'])
        self.table.setStyleSheet('background-color: white; border-radius: 5px;')
        layout.addWidget(self.table)

    def load_products(self):
        # TODO: Implement loading products from database
        pass

    def add_product(self):
        dialog = ProductDialog(self)
        if dialog.exec_():
            product_data = dialog.get_product_data()
            # TODO: Add product to database
            self.load_products()

    def edit_product(self, product_id):
        # TODO: Implement edit product
        pass

    def delete_product(self, product_id):
        # TODO: Implement delete product
        pass
