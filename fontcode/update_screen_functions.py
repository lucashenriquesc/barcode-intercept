import power as power
def clear_edit_screen(self):
    """Deleta widgets dos layouts da tela de edição de código"""
    clear_edit_label_layout(self)
    clear_product_code_layout(self)
    clear_internal_code_layout(self)
    clear_barcode_layout(self)
    clear_edit_button_layout(self)
    clear_remove_button_layout(self)
    clear_edit_label_outcome_layout(self)

def clear_add_screen(self):
    """Deleta widgets dos layouts da tela de adição de códigos"""
    clear_add_label_layout(self)
    clear_add_product_code_layout(self)
    clear_add_internal_code_layout(self)
    clear_add_barcode_layout(self)
    clear_add_button_layout(self)
    clear_add_outcome_label_layout(self)

    ####Remove widgets dos layouts das telas.
def clear_clicked_layout(self):
    """Limpa o layout principal da tela de edição de códigos"""
    while self.clicked_layout.count():
        item = self.clicked_layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()
def clear_items_layout(self):
    """Limpa o layout de cada widget de botão na tela principal de visualização de códigos cadastrados"""
    while self.items_layout.count():
        item = self.items_layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()

    ####Funções de limpeza de layout na tela de edição de códigos.
def clear_edit_label_layout(self):
    """Limpa os widgets do layout da label principal na tela de edição de códigos."""
    while self.edit_label_layout.count():
        item = self.edit_label_layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()
def clear_product_code_layout(self):
    """Limpa os widgets do layout de código de produto na tela de edição de códigos."""
    while self.product_code_layout.count():
        item = self.product_code_layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()
def clear_internal_code_layout(self):
    """Limpa os widgets do layout de código interno na tela de edição de códigos."""
    while self.internal_code_layout.count():
        item = self.internal_code_layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()
def clear_barcode_layout(self):
    """Limpa os widgets do layout de código de barras na tela de edição de códigos."""
    while self.barcode_layout.count():
        item = self.barcode_layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()
def clear_edit_button_layout(self):
    """Limpa os widgets do layout do botão que aplica a edição do código feita pelo usuário."""
    while self.edit_button_layout.count():
        item = self.edit_button_layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()
def clear_remove_button_layout(self):
    """Limpa os widgets do botão que faz a remoção de códigos escolhida pelo usuário."""
    while self.delete_button_layout.count():
        item = self.delete_button_layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()
def clear_edit_label_outcome_layout(self):
    """Limpa os widgets da label que mostra o retorno da ação do usuário na tela de edição."""
    while self.edit_outcome_label_layout.count():
        item = self.edit_outcome_label_layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()
 
    ####Funções de limpeza de layout na tela de adição de códigos.
def clear_add_layout(self):
    """Limpa os widgets do layout principal da tela de adição de códigos."""
    while self.add_layout.count():
        item = self.add_layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()
def clear_add_label_layout(self):
    """Limpa os widgets do layout da label principão da tela de adição de códigos."""
    while self.add_label_layout.count():
        item = self.add_label_layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()
def clear_add_product_code_layout(self):
    """Limpa os widgets do layout de código do produto na tela de adição de códigos."""
    while self.add_product_code_layout.count():
        item = self.add_product_code_layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()
def clear_add_internal_code_layout(self):
    """Limpa os widgets do layout do código interno na tela de adição de códigos."""
    while self.add_internal_code_layout.count():
        item = self.add_internal_code_layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()
def clear_add_barcode_layout(self):
    """Limpa os widgets do layout de código de barras na tela de adição de códigos."""
    while self.add_barcode_layout.count():
        item = self.add_barcode_layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()
def clear_add_button_layout(self):
    """Limpa os widgets do layout do botão de adição de códigos"""
    while self.add_button_layout.count():
        item = self.add_button_layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()
def clear_add_outcome_label_layout(self):
    """Limpa os widgets do layout da label que mostra o retorno da ação do usuário na tela de adição de códigos."""
    while self.add_outcome_label_layout.count():
        item = self.add_outcome_label_layout.takeAt(0)
        widget = item.widget()
        if widget:
            widget.deleteLater()
    ####Atualiza os items na tela
def refresh_screen(self):
    """Atualiza a tela e reinicia o hook de barcodes"""
    try:
        power.kill_barcode(self)
    except Exception as e:
        print(e)
    power.start_barcode(self)
    self.load_codes()
    clear_items_layout(self)
    self.load_items()
def refresh_on_power(self):
    self.load_codes()
    clear_items_layout(self)
    self.load_items()