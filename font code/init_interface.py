from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QScrollArea, QMainWindow, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
def init_interfaces(self):
    #Window, widgets and layouts
    self.window = QMainWindow(); self.window.setFixedWidth(450); self.window.setFixedHeight(550) #Main window ##750/550
    self.window.setWindowTitle('Barcode Intercept - By Lucas')
    self.widget = QWidget() #Main window Widget
    self.adding_window = QWidget(); self.adding_window.setFixedWidth(400); self.adding_window.setFixedHeight(500) #Adding window widget
    self.adding_window.setWindowTitle('Adicionar peça')
    self.clicked_layout = QVBoxLayout(); self.clicked_layout.setAlignment(Qt.AlignTop) #Clicked layout
    self.add_layout = QVBoxLayout(); self.add_layout.setAlignment(Qt.AlignTop) #Add layout
    self.item_window = QWidget(); self.item_window.setFixedWidth(400); self.item_window.setFixedHeight(500) #Item window
    self.item_window.setWindowTitle('Editar ou remover peça')
    self.items_widget = QWidget() #Items widget
    self.items_scrollarea = QScrollArea(); self.items_scrollarea.setWidgetResizable(True) #Main widget central widget, scrollarea
    #Add item button and start/stop button
    self.power_button = QPushButton('LIGADO'); self.power_button.clicked.connect(self.power); self.power_button.setFixedHeight(50)
    self.power_button.setStyleSheet('font-size:22px; background-color:rgb(150,255,150)')
    self.add_button = QPushButton('ADICIONAR PEÇA'); self.add_button.clicked.connect(self.add_function); self.add_button.setFixedHeight(50)
    self.add_button.setStyleSheet('font-size:22px; background-color:rgb(200,200,255)')
    #Main Buttons layout
    self.main_buttons_layout = QHBoxLayout(); #self.main_buttons_layout.setAlignment(Qt.AlignCenter)
    self.main_buttons_layout.addWidget(self.power_button)
    self.main_buttons_layout.addWidget(self.add_button)
    #Search field 
    self.search_field = QLineEdit()
    self.search_field.textChanged.connect(self.search)
    self.search_field.setStyleSheet("""QLineEdit{border: 1px solid rgb(100, 100, 200);border-radius: 5px; padding: 5px;}""")
    self.search_field.setPlaceholderText("Busca")
    #Creating main layout and adding buttons to it.
    self.layout = QVBoxLayout(); self.layout.addLayout(self.main_buttons_layout) #Main layout
    self.layout.addWidget(self.search_field)
    self.items_layout = QVBoxLayout(); #Items layout
    self.items_layout.setAlignment(Qt.AlignTop)

