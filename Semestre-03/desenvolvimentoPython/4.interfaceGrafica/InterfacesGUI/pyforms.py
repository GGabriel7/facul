import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton

class ExemploSimples(BaseWidget):

    def __init__(self):
        super(ExemploSimples,self).__init__('ExemploSimples')
        #Definition of the forms fields
        self._nome = ControlText('Nome', 'Default value')
        self._sobrename = ControlText('Sobrenome')
        self._nomeCompleto = ControlText('Nome completo')
        self._button = ControlButton('Pressione o Botão')


#Execute the application
if __name__ == " __main__":
    from pyforms import start_app
    start_app(ExemploSimples)
    
# PyForms é um framework Python para o desenvolvimento rápido de aplicações GUI. Ele é construído sobre bibliotecas como PyQt ou wxPython, facilitando a criação de interfaces gráficas de usuário com menos código e maior produtividade.