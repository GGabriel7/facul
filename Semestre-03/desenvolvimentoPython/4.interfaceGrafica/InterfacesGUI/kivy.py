from kivy.app import App
from kivy.uix.button import Button

class ExemploApp(App):
    def build(self):
        return Button(text='Olá, Mundo!')
    
# Kivy é uma biblioteca de código aberto para o desenvolvimento de aplicações multi-toque. Ela é usada para criar interfaces gráficas de usuário (GUIs) que podem ser executadas em várias plataformas, incluindo Windows, macOS, Linux, Android e iOS.