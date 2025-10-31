import wx
class Janela(wx.Frame):
   def __init__(self, parent, title):
      super(Janela, self).__init__(parent, title=title, size = (400,300))
      self.panel = ExemploPainel(self)
      self.text_ctrl = wx.TextCtrl(self.panel, pos=(5, 5))
      self.btn_test = wx.Button(self.panel, label='Pressione esse componente!', pos=(5, 55))


class ExemploPainel(wx.Panel):
   def __init__(self, parent):
      super(ExemploPainel, self).__init__(parent)


class ExemploApp(wx.App):
   def OnInit(self):
      self.frame = Janela(parent=None, title="Janela wxPython")
      self.frame.Show()
      return True


app = ExemploApp()
app.MainLoop()

# wxPython é um conjunto de ligações Python para a biblioteca GUI wxWidgets, permitindo a criação de aplicações com interfaces gráficas nativas em várias plataformas, como Windows, macOS e Linux. É amplamente utilizado para desenvolver aplicações desktop com uma aparência consistente e funcionalidade rica.