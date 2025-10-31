from flexx import flx
class Exemplo(flx.Widget):

    def init(self):
        flx.Button(text='Olá')
        flx.Button(text='Mundo')

if __name__ == '__main__':
    a = flx.App(Exemplo, title='Flexx demonstração')
    m = a.launch()
    flx.run()
    
# flexx é um framework para criar aplicações web usando Python. Ele permite que você escreva a lógica da aplicação em Python, enquanto a interface do usuário é renderizada em HTML/CSS/JavaScript no navegador.
# utilizada tanto para aplicações desktop quanto web.
# 