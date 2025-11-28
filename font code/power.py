import psutil
from PyQt5.QtCore import QProcess
import update_screen_functions as upsf

def kill_barcode(self):
    self.pid = self.p.processId()
    try:
        self.parent = psutil.Process(self.pid)
        for child in self.parent.children(recursive=True):
            child.terminate()  
        self.parent.terminate() 
    except Exception as e: #psutil.NoSuchProcess:
        pass  
def start_barcode(self):
    if self.power_button.text() == 'LIGADO':
        try:
            self.p = QProcess()
            self.p.start('barcode.exe') 
        except Exception as e:
            print(e)
    else:
        pass


