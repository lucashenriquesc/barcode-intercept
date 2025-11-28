from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
def edit_screen_layouts(self):
    self.edit_label_layout = QHBoxLayout(); self.edit_label_layout.setAlignment(Qt.AlignCenter)
    self.product_code_layout = QHBoxLayout(); self.internal_code_layout = QHBoxLayout()
    self.barcode_layout = QHBoxLayout(); self.edit_button_layout = QHBoxLayout()
    self.delete_button_layout = QHBoxLayout(); self.edit_outcome_label_layout = QHBoxLayout()
    self.edit_outcome_label_layout.setAlignment(Qt.AlignCenter)  
    self.product_code_layout.setAlignment(Qt.AlignCenter)
    self.internal_code_layout.setAlignment(Qt.AlignCenter)
    self.barcode_layout.setAlignment(Qt.AlignCenter)
def edit_screen_items(self):
    self.edit_label = QLabel(); self.edit_label.setAlignment(Qt.AlignCenter)
    self.product_code_label = QLabel() ;self.product_code_input = QLineEdit(); 
    self.internal_code_label = QLabel(); self.internal_code_input = QLineEdit(); 
    self.barcode_label = QLabel(); self.barcode_input = QLineEdit()
    self.edit_button = QPushButton(); self.edit_button.clicked.connect(self.edit_code)
    self.edit_button.setFixedHeight(50); self.edit_button.setStyleSheet('font-size:18px; background-color:rgb(190,255,190)')
    self.delete_button = QPushButton(); self.delete_button.clicked.connect(self.code_delete)
    self.edit_outcome_label = QLabel(); self.edit_outcome_label.setAlignment(Qt.AlignCenter)
    self.edit_outcome_label.setStyleSheet('font-size:15px; font-weight:bold')
    self.delete_button.setFixedHeight(50); self.delete_button.setStyleSheet('font-size:18px; background-color:rgb(255,190,190)')
    ###Alignments
    self.product_code_input.setAlignment(Qt.AlignCenter); self.product_code_label.setAlignment(Qt.AlignCenter)
    self.product_code_input.setFixedWidth(175); self.product_code_label.setFixedWidth(175)
    self.product_code_input.setFixedHeight(30); self.product_code_label.setFixedHeight(25)

    self.internal_code_input.setAlignment(Qt.AlignCenter); self.internal_code_label.setAlignment(Qt.AlignCenter)
    self.internal_code_input.setFixedWidth(175); self.internal_code_label.setFixedWidth(175)
    self.internal_code_input.setFixedHeight(30); self.internal_code_label.setFixedHeight(25)

    self.barcode_input.setAlignment(Qt.AlignCenter); self.barcode_label.setAlignment(Qt.AlignCenter)
    self.barcode_input.setFixedWidth(175); self.barcode_label.setFixedWidth(175)
    self.barcode_input.setFixedHeight(30); self.barcode_label.setFixedHeight(25)

    