from pywinauto.application import Application

app = Application(backend='uia').start("calc.exe")

app.C.click()