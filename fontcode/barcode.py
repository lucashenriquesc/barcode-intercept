import os
import keyboard
import mouse
import csv

class barcode():
    """A barcode scanner intercepter, developed to try to get around barcodes that aren't correctly registered in Palusa's database."""
    def __init__(self):
        """Initiate main variables, for storing filepaths and values in the database"""
        self.filepath = os.getcwd() + "/files/barcodes.txt"
        self.barcode_reset_keys_filepath = os.getcwd() + "/files/keys.txt"
        self.invalid_barcodes = {}
        self.barcode = ''
        self.product_code = {}
        self.special = ['!', '@', '$', '%', '¨', '&', '*', '(', ')', 'up', 'down', 'left', 'right', 'page down', 'page up', 'print screen', 'scroll lock', 'end', 'home', 'insert']
        self.barcode_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '#']
        self.keys = ['enter']
        self.barcode_reset_keys = []
    def load_codes(self):
        """Load the file with the barcodes that arent recognized by the system."""
        with open(self.filepath, 'r+') as f:
            reader = csv.reader(f)
            header_row = next(reader)
            #print("Produtos cadastrados: ")
            for row in reader:
                self.invalid_barcodes[row[0].strip()] = row[1].strip()
                self.product_code[row[2].strip()] = row[1].strip()
                #print("Peça: " + row[2].strip().upper() + "| Código de Barras: " + row[0].strip() + "| Código interno: " + row[1].strip())
    def load_keys(self):
        with open(self.barcode_reset_keys_filepath, 'r') as f:
            for row in csv.reader(f):
                for key in row: 
                    pass
                    self.barcode_reset_keys.append(key.strip())
    def on_mouse_event(self, event):
        """Mouse event monitoring - Clears the barcode input field if left mouse button is pressed, 
        for trying to prevent undesired numbers and chars to be concatenated to the barcode variable"""
        if mouse.is_pressed(button='left'):
            self.barcode = ''
    def barcode_key_event(self, event):
        """Keyboard keypress monitoring for evaluating decisions based on barcode scanner/user inpu ts."""
        if event.event_type == 'down':
            if event.name == 'enter' and self.barcode in self.invalid_barcodes.keys(): #Caso input seja ENTER, e o barcode ESTÁ no arquivo de codígo de barras que não funciona
                self.clear_field()
                self.barcode_replace(event)
            elif event.name == 'enter' and self.barcode not in self.invalid_barcodes.keys(): #Caso input seja ENTER, e o barcode NÃO ESTÁ no arquivo de códigos que não funcionam
                keyboard.press(event.scan_code)
                self.barcode = ''
            elif event.name in self.barcode_keys: #Verifica se o nome da tecla pressionada é um número ou caracter válido.
                self.barcode += event.name
                keyboard.press(event.name)
            elif event.name in self.special:
                keyboard.press(event.name)     
        if event.event_type == 'up':
            keyboard.release(event.name)  
    def clear_field(self):
        """Clears the barcode input field after detected that a non-functional code was sent by user/barcode scanner."""
        keyboard.press('ctrl'); keyboard.press('a'); keyboard.press('backspace')
        keyboard.release('ctrl'); keyboard.release('a'); keyboard.release('backspace')
    def barcode_replace(self, event):
        """Replaces a code marked as non-functional with an internal code."""
        self.barcode = str(self.invalid_barcodes[self.barcode])
        for number in list(self.barcode):
            keyboard.press_and_release(number)
        keyboard.press(event.scan_code)
        keyboard.release(event.scan_code)
        self.barcode = ''
    def clear_barcode(self, event):
        if event.event_type == 'down' and event.name in self.barcode_reset_keys:
            if event.name == 'shift':
                pass
            else:
                self.barcode = ''
        elif event.event_type == 'up' and event.name in self.barcode_reset_keys:
            pass
    def exec_keyhook(self):
        """Starts the main hooks for mouse/keyboard inputs monitoring."""
        mouse.hook(self.on_mouse_event)
        for key in self.barcode_keys:
            keyboard.hook_key(key, self.barcode_key_event, suppress=True)
        for sp in self.special:
            keyboard.hook_key(sp, self.barcode_key_event, suppress=True)
        for nb in self.keys:
            keyboard.hook_key(nb, self.barcode_key_event, suppress=True)
        for key in self.barcode_reset_keys:
            keyboard.hook_key(key, self.clear_barcode, suppress=False)
        keyboard.wait(None)

intercepter = barcode()
intercepter.load_keys()
intercepter.load_codes()
intercepter.exec_keyhook() 









































