from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
def add_screen_layouts(self):
    self.add_label_layout = QHBoxLayout(); self.add_label_layout.setAlignment(Qt.AlignCenter)
    self.add_product_code_layout = QHBoxLayout(); self.add_product_code_layout.setAlignment(Qt.AlignCenter)
    self.add_internal_code_layout = QHBoxLayout(); self.add_internal_code_layout.setAlignment(Qt.AlignCenter)
    self.add_barcode_layout = QHBoxLayout(); self.add_barcode_layout.setAlignment(Qt.AlignCenter)
    self.add_button_layout = QHBoxLayout()
    self.add_outcome_label_layout = QHBoxLayout()
    self.add_outcome_label_layout.setAlignment(Qt.AlignCenter); self.add_outcome_label.setText('')
    self.add_product_code_layout.setAlignment(Qt.AlignCenter)
    self.add_internal_code_layout.setAlignment(Qt.AlignCenter)
    self.add_barcode_layout.setAlignment(Qt.AlignCenter)
def add_screen_items(self):
    self.add_label = QLabel()
    self.add_product_code_label = QLabel(); self.add_product_code_input = QLineEdit()
    self.add_internal_code_label = QLabel(); self.add_internal_code_input = QLineEdit()
    self.add_barcode_label = QLabel(); self.add_barcode_input = QLineEdit()
    self.add_item_button = QPushButton(); self.add_item_button.clicked.connect(self.add_values)
    self.add_outcome_label = QLabel(); self.add_outcome_label.setStyleSheet('font-size:15px; font-weight:bold')
    
    self.add_product_code_input.setAlignment(Qt.AlignCenter); self.add_product_code_label.setAlignment(Qt.AlignCenter)
    self.add_product_code_input.setFixedWidth(175); self.add_product_code_label.setFixedWidth(175)
    self.add_product_code_input.setFixedHeight(30); self.add_product_code_label.setFixedHeight(25)

    self.add_internal_code_input.setAlignment(Qt.AlignCenter); self.add_internal_code_label.setAlignment(Qt.AlignCenter)
    self.add_internal_code_input.setFixedWidth(175); self.add_internal_code_label.setFixedWidth(175)
    self.add_internal_code_input.setFixedHeight(30); self.add_internal_code_label.setFixedHeight(25)

    self.add_barcode_input.setAlignment(Qt.AlignCenter); self.add_barcode_label.setAlignment(Qt.AlignCenter)
    self.add_barcode_input.setFixedWidth(175); self.add_barcode_label.setFixedWidth(175)
    self.add_barcode_input.setFixedHeight(30); self.add_barcode_label.setFixedHeight(25)