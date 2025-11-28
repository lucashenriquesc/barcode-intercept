import PyQt5.QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QScrollArea, QMainWindow, QHBoxLayout, QStyleFactory, QLineEdit, QAction, QMessageBox
from PyQt5.QtCore import Qt, QProcess, QTimer
from PyQt5.QtGui import QFont, QIcon
import signal
import os
import csv
import psutil
import update_screen_functions as upsf
import edit_screen_widgets_layouts as edit
import add_screen_widgets_layouts as add
import init_interface as inter_init
import power as power
import re

class interface():
    def __init__(self):
        """Initiate main variables for file loading and filepaths"""
        self.app = QApplication([]) #Starts que QA
        self.app.setStyle(QStyleFactory.create("Fusion"))
        self.invalid_barcodes = {}
        self.ico_filepath = os.getcwd() + "/files/images/ico/barcode.jpg"
        self.product_code = []
        self.product_infos = []
        self.prod_info_code = {}
        self.products_objects = {}
        self.filepath = os.getcwd() + "/files/barcodes.txt"
        self.barcode_filepath = os.getcwd() + "/barcode.exe"
        self.app.setWindowIcon(QIcon(self.ico_filepath))
        inter_init.init_interfaces(self)
        self.load_codes()
        power.start_barcode(self)
        self.load_items()
        #Items showing
        self.items_widget.setLayout(self.items_layout)
        self.items_scrollarea.setWidget(self.items_widget)
        self.layout.addWidget(self.items_scrollarea)
        #Setting Widget layout
        self.widget.setLayout(self.layout)
        #Scrollarea
        self.scroll = QScrollArea()
        self.app.setStyleSheet("QWidget{font-size: 17px;font-family: Arial;font-weight: bold;color: rgb(0, 0, 0);background-color: rgb(204,229,255)}")
        self.scroll.setWidget(self.widget)
        self.scroll.setWidgetResizable(True)
        #Window central widget and show function
        self.window.setCentralWidget(self.scroll)
        #Edit screen
        add.add_screen_items(self)
        add.add_screen_layouts(self)
        edit.edit_screen_items(self)
        edit.edit_screen_layouts(self)
        #Show window
        self.window.show()
        self.window.raise_()
        self.window.showNormal()
    def exec(self):
        """Exec the app."""
        self.app.exec()
    def format_database(self):
        """Load the barcodes file and apply strip function to its lines to reduce chance of failing when reading the codes."""
        data = ''
        with open(self.filepath, 'r+') as f:
            for line in f.readlines():
                try:
                    if line.strip() != '':
                        data += line.strip() + "\n"
                    elif line.strip() == '':
                        continue
                except:
                    continue
        with open(self.filepath, 'w') as f:
            f.write(data.strip())
    def load_codes(self):
        """Load the formated file containing the barcodes that aren't recognized by the system."""
        prod_info_code = {}
        i = 0
        self.format_database()
        with open(self.filepath, 'r') as f:
            next(f)
            for row in csv.reader(f):
                try:
                    self.product_code = i, row[2].strip()
                    self.product_infos = [row[0].strip(), row[1].strip()]
                    prod_info_code[self.product_code] = self.product_infos
                    i += 1
                except:
                    continue
        self.prod_info_code = prod_info_code
    def load_items(self):
        """Carrega os códigos na tela principal."""
        for prod_code, prod_info in self.prod_info_code.items():
            ###Create a new label and configure text and other options
            self.label = QLabel()
            self.label.setAttribute(Qt.WA_TransparentForMouseEvents)
            self.label.setText("Peça: <span style='color:red;'>" + str(prod_code[1]).upper() + "</span><br>Código interno: " + "<span style='color:red;'>" +prod_info[1] + "</span>" + "<br>Código de barras: " + "<span style='color:red;'>" +prod_info[0] + "</span>")
            self.label.setFixedHeight(65)
            self.label.setStyleSheet("background-color: transparent;")
            self.label.setAlignment(Qt.AlignCenter)
            ###Embed the label inside the layout and the layout inside the button.
            self.item=QPushButton('')
            self.item.setFixedHeight(80)
            self.lay = QVBoxLayout()
            self.lay.addWidget(self.label)
            self.item.setLayout(self.lay)
            self.item.clicked.connect(self.on_button_click)
            self.products_objects[self.item] = prod_code[0], prod_code[1], prod_info[0], prod_info[1]
            self.items_layout.addWidget(self.item)
    def load_item_codes(self, clicked):
        for key, value in self.products_objects.items():
            if clicked == key:
                code = value[1].strip()
                internal = value[3]
                barcode = value[2]
                index = value[0]
                return code, internal, barcode, index
    def on_button_click(self):
        self.deleted_code = ''
        upsf.clear_edit_screen(self)
        edit.edit_screen_items(self)
        edit.edit_screen_layouts(self)
        upsf.clear_clicked_layout(self)
        self.clicked = self.item.sender()
        self.code, internal, barcode, index = self.load_item_codes(self.clicked)
        #Changing infos label and layout
        self.edit_label.setText('EDIÇAO DE CÓDIGO \nPEÇA: ' + self.code); self.edit_label.setStyleSheet('font-size:19px; font-weight:bold; color:red')
        self.edit_label_layout.addWidget(self.edit_label)
        #Product code label and entry field:
        self.product_code_label.setText("Código da peça "); self.product_code_label.setStyleSheet('font-size:18px; font-weight:bold')
        self.product_code_input.setText(self.code)
        self.product_code_layout.addWidget(self.product_code_label)
        self.product_code_layout.addWidget(self.product_code_input)
        #Internal code label and entry field:
        self.internal_code_label.setText('Código interno '); self.internal_code_label.setStyleSheet('font-size:18px; font-weight:bold')
        self.internal_code_input.setText(internal)
        self.internal_code_layout.addWidget(self.internal_code_label)
        self.internal_code_layout.addWidget(self.internal_code_input)
        #Barcode label and entry field:
        self.barcode_label.setText('Código de barras ')
        self.barcode_label.setStyleSheet('font-size:18px; font-weight:bold')
        self.barcode_input.setText(barcode)
        self.barcode_layout.addWidget(self.barcode_label)
        self.barcode_layout.addWidget(self.barcode_input)
        #Edit button
        self.edit_button.setText('Salvar alterações')
        self.edit_button_layout.addWidget(self.edit_button)
        #Delete button
        self.delete_button.setText('Excluir código')
        self.delete_button_layout.addWidget(self.delete_button)
        #Add outcome label
        self.edit_outcome_label_layout.addWidget(self.edit_outcome_label)
        #Adding 
        self.clicked_layout.addLayout(self.edit_label_layout)
        self.clicked_layout.addLayout(self.product_code_layout)
        self.clicked_layout.addLayout(self.internal_code_layout)
        self.clicked_layout.addLayout(self.barcode_layout)
        self.clicked_layout.addLayout(self.edit_button_layout)
        self.clicked_layout.addLayout(self.delete_button_layout)
        self.clicked_layout.addLayout(self.edit_outcome_label_layout)
        #Showing edit window and setting layout
        self.item_window.setLayout(self.clicked_layout)
        self.item_window.show()
        self.item_window.raise_()
        self.item_window.showNormal()
    ###Editing code functions
    def edit_code(self):
        """Substitui os valores dos códigos escolhidos pelo usuário"""
        return_text = ''
        self.edit_outcome_label.setText('')
        self.code, self.internal, self.barcode, self.index = self.load_item_codes(self.clicked)
        self.old_product_code = ''; self.old_internal = ''; self.old_barcode = ''
        self.new_product_code = str(self.product_code_input.text().strip().upper())
        self.new_barcode = str(self.barcode_input.text().strip().upper())
        self.new_internal_code = str(self.internal_code_input.text().strip().upper())
        with open(self.filepath, 'r') as inf:
            for row in csv.reader(inf):
                if self.code == row[2].strip() and self.internal == row[1].strip() and self.barcode == row[0].strip():
                    self.old_barcode = row[0].strip()
                    self.old_internal = row[1].strip()
                    self.old_product_code = row[2].upper().strip()
                    break
        if not self.old_product_code and not self.old_internal and not self.old_barcode:
            return_text = ("<br>PEÇA: " + "<span style='color:red;'>" + self.code.upper().strip() + "</span>" + "<br> NÃO ENCONTRADA NO BANCO DE DADOS!")
            self.edit_print_outcome_label(return_text)
        if self.new_product_code == self.code and self.new_internal_code == self.old_internal and self.new_barcode == self.old_barcode:
            return_text += ("\nMODIFIQUE ALGUM ATRIBUTO ANTES DE SALVAR!")
            self.edit_print_outcome_label(return_text)
        with open(self.filepath, 'r') as inf:
            reader = csv.reader(inf)
            for row in reader:
                try:
                    if self.new_barcode != self.old_barcode and self.new_barcode == row[0]:
                        return_text += ("<br>CÓDIGO DE BARRAS: " + "<span style='color:red;'>" + self.new_barcode + "</span>" + "<br>JÁ ESTÁ CADASTRADO! <br>PEÇA: " + "<span style='color:red;'>" + row[2].upper().strip() + "</span>" + "<br>CÓDIGO INTERNO: " + "<span style='color:red;'>" + row[1].upper().strip()+ "</span>" + "<br>")
                        self.edit_print_outcome_label(return_text)
                except Exception as e: 
                    continue
        if return_text == '':
            self.write_editing()
        else:
            self.edit_print_outcome_label(return_text)

    def write_editing(self):
        with open(self.filepath, 'r') as inf:
            file = inf.read()
            file = re.sub(rf'\b{re.escape(self.old_barcode)}\b', self.new_barcode, file)
            file = re.sub(rf'\b{re.escape(self.old_internal)}\b', self.new_internal_code, file)
            file = re.sub(rf'\b{re.escape(self.code)}\b', self.new_product_code, file)
        with open(self.filepath, 'w') as outf:
            outf.write(file)
        self.code = self.new_product_code
        self.products_objects[self.clicked] = self.index, self.new_product_code, self.new_barcode, self.new_internal_code
        self.edit_label.setText('EDITANDO CÓDIGO \nPEÇA: ' + self.new_product_code)
        return_text = ("\nALTERAÇÕES SALVAS!")
        self.edit_print_outcome_label(return_text)
        try:
            upsf.refresh_screen(self)
        except Exception as e:
            print((e))
        
    ###Deleting code functions    
    def code_delete(self):
        """Procura pelo codigo no banco de dados e o deleta, se existente."""
        file_to_write = ''
        self.code, internal, barcode, self.index = self.load_item_codes(self.clicked)
        self.deleted_code = ''
        internal = self.internal_code_input.text().strip().upper()
        barcode = self.barcode_input.text().strip().upper()
        
        with open(self.filepath, 'r') as inf:
            for line in csv.reader(inf):
                if self.code == line[2].strip() and internal == line[1].strip() and barcode == line[0].strip():
                    self.deleted_code = self.code  
                if (self.code == line[2].strip() or self.code != line[2].strip()) and internal != line[1] and barcode != line[0]:
                    file_to_write += str(line[0]) + "," + str(line[1]) + "," + str(line[2] + "\n")
                
        if self.deleted_code == '':
            return_text = ("<br>PEÇA: " + "<span style='color:red;'>" + self.code.upper().strip() + "</span>" + "<br> NÃO ENCONTRADA NO BANCO DE DADOS!")
            self.edit_print_outcome_label(return_text)
        else:
            self.delete_write(file_to_write)

    def delete_write(self, file):
        """Se localizado, grava o novo arquivo sem o código apagado"""
        with open(self.filepath, 'w') as outf:
            outf.write(file) 
        return_text = ("<br>PEÇA " + "<span style='color:red;'>" + self.code + "</span>" + " REMOVIDA!")
        self.edit_print_outcome_label(return_text)
        upsf.refresh_screen(self)
    
    def power(self):    
        """Liga ou desliga o programa."""
        state = self.power_button.sender()
        if state.text() == 'LIGADO':
            upsf.refresh_on_power(self)
            self.power_button.setText('DESLIGADO')
            power.kill_barcode(self)
            self.power_button.setStyleSheet('font-size:25px; background-color:rgb(255,150,150)')
        elif state.text() == 'DESLIGADO':
            upsf.refresh_on_power(self)
            self.power_button.setText('LIGADO')
            power.start_barcode(self)
            self.power_button.setStyleSheet('font-size:25px; background-color:rgb(150,255,150)')
        
    ###Adding code functions
    def add_function(self):
        upsf.clear_add_screen(self)
        add.add_screen_layouts(self); add.add_screen_items(self)
        upsf.clear_add_layout(self)
        #editing label text and layout
        self.add_label.setText('ADICIONAR CÓDIGO')
        self.add_label.setStyleSheet('font-size:19px; font-weight:bold; color:red')
        self.add_label_layout.addWidget(self.add_label)
        #product code text and layout
        self.add_product_code_label.setText('Código da peça ')
        self.add_product_code_label.setStyleSheet('font-size:18px; font-weight:bold')
        self.add_product_code_input.setText('')
        self.add_product_code_layout.addWidget(self.add_product_code_label)
        self.add_product_code_layout.addWidget(self.add_product_code_input)
        #internal code text and layout
        self.add_internal_code_label.setText('Código interno ')
        self.add_internal_code_label.setStyleSheet('font-size:18px; font-weight:bold')
        self.add_internal_code_input.setText('')
        self.add_internal_code_layout.addWidget(self.add_internal_code_label)
        self.add_internal_code_layout.addWidget(self.add_internal_code_input)
        #barcode text and layout
        self.add_barcode_label.setText('Código de barras ')
        self.add_barcode_label.setStyleSheet('font-size:18px; font-weight:bold')
        self.add_barcode_input.setText('')
        self.add_barcode_layout.addWidget(self.add_barcode_label)
        self.add_barcode_layout.addWidget(self.add_barcode_input)
        #add button
        self.add_item_button.setStyleSheet('font-size:18px; background-color:rgb(180,228,255)')
        self.add_item_button.setFixedHeight(50)
        self.add_button_layout.addWidget(self.add_item_button)
        self.add_item_button.setText('Adicionar peça')
        #Add outome label 
        self.add_outcome_label_layout.addWidget(self.add_outcome_label)
        #adding
        self.add_layout.addLayout(self.add_label_layout)
        self.add_layout.addLayout(self.add_product_code_layout)
        self.add_layout.addLayout(self.add_internal_code_layout)
        self.add_layout.addLayout(self.add_barcode_layout)
        self.add_layout.addLayout(self.add_button_layout)
        self.add_layout.addLayout(self.add_outcome_label_layout)
        #settings addingwindow layout
        self.adding_window.setLayout(self.add_layout)
        self.add_barcode_input.setFocus()
        #adding window show
        self.adding_window.show()
        self.adding_window.raise_()
        self.adding_window.showNormal()
    def add_values(self):
        return_text = ''
        empty = ''
        self.add_outcome_label.setText('')
        self.add_product_code = str(self.add_product_code_input.text().upper().strip())
        self.add_internal_code = str(self.add_internal_code_input.text().upper().strip())
        self.add_barcode = str(self.add_barcode_input.text().upper().strip())

        if self.add_product_code != '' and self.add_internal_code != '' and self.add_barcode != '':
            with open(self.filepath, 'r') as inf:
                file = csv.reader(inf)
                for row in file:
                    try:
                        if self.add_barcode == row[0].upper().strip():
                            return_text += ("<br>CÓDIGO DE BARRAS: " + "<span style='color:red;'>" + self.add_barcode + "</span>" +"<br>JÁ ESTÁ CADASTRADO! <br>PEÇA: " + "<span style='color:red;'>" + row[2].upper().strip() + "</span>" + "<br>CÓDIGO INTERNO: " + "<span style='color:red;'>" + row[1].upper().strip()) + "</span>" + "<br>"
                    except:
                        continue
            if not return_text:
                self.add_write()
            else:
                self.add_print_outcome_label(return_text)
        else:
            if not self.add_product_code:
                empty += ("<br><span style='color:red;'>" + "CÓDIGO DA PEÇA NÃO PODE ESTAR VAZIO!" + "</span>")
            if not self.add_internal_code:
                empty += ("<br><span style='color:red;'>" + "CÓDIGO INTERNO NÃO PODE ESTAR VAZIO!" + "</span>")
            if not self.add_barcode:
                empty += ("<br><span style='color:red;'>" + "CÓDIGO DE BARRAS NÃO PODE ESTAR VAZIO!" + "</span>")    
            self.add_print_outcome_label(empty)
            upsf.refresh_screen(self)
    def add_write(self):
        """Grava o novo código adicionado no arquivo de códigos."""
        with open(self.filepath, 'a') as outf:
            outf.write('\n' + self.add_barcode + ', ' + self.add_internal_code + ', ' + self.add_product_code)
        return_text = ("<br>CADASTRO DA PEÇA <span style='color:red;'>" + self.add_product_code + "</span> EFETUADO!")
        self.add_print_outcome_label(return_text)
        upsf.refresh_screen(self)
    def search(self):
        """Função de buscar items/códigos na tela principal da interface."""
        upsf.clear_items_layout(self)
        search_input = self.search_field.text().upper()
        for prod_code, prod_info in self.prod_info_code.items():
            if search_input in prod_code[1].upper() or search_input in prod_info[1].upper() or search_input in prod_info[0].upper():
                ###Create a new label and configure text and other options
                self.label = QLabel()
                self.label.setAttribute(Qt.WA_TransparentForMouseEvents)
                self.label.setText("Peça: <span style='color:red;'>" + str(prod_code[1]).upper() + "</span><br>Código interno: " + "<span style='color:red;'>" +prod_info[1] + "</span>" + "<br>Código de barras: " + "<span style='color:red;'>" +prod_info[0] + "</span>")
                self.label.setFixedHeight(65)
                self.label.setStyleSheet("background-color: transparent")
                self.label.setAlignment(Qt.AlignCenter)
                ###Embed the label inside the layout and the layout inside the button.
                self.item=QPushButton('')
                self.item.setFixedHeight(80)
                self.lay = QVBoxLayout()
                self.lay.addWidget(self.label)
                self.item.setLayout(self.lay)
                self.item.clicked.connect(self.on_button_click)
                self.products_objects[self.item] = prod_code[0], prod_code[1], prod_info[0], prod_info[1]
                self.items_layout.addWidget(self.item)
    def edit_print_outcome_label(self, return_text):
        """Determina o texto e o estilo do texto da label de resposta da tela de edição de códigos."""
        self.edit_outcome_label.setStyleSheet('font-size:15px; font-weight:bold')
        self.edit_outcome_label.setText(return_text)
        QTimer.singleShot(6000, lambda: self.edit_outcome_label.setText(''))
    def add_print_outcome_label(self, return_text):
        """Determina o texto e o estilo do texto da label de resposta da tela de adição de códigos."""
        self.add_outcome_label.setStyleSheet('font-size:15px; font-weight:bold')
        self.add_outcome_label.setText(return_text)
        QTimer.singleShot(6000, lambda: self.add_outcome_label.setText(''))
    ###Close Event
    def new_close_event(self, event):
        """Fecha o barcode.exe ao fechar a interface"""
        power.kill_barcode(self)
 
screen = interface()
screen.window.closeEvent = screen.new_close_event
screen.exec()