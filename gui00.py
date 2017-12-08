import wx
class MyApp(wx.App): # создаем класс оконной программы
  def OnInit(self): # инициализация программы
      self.frame = MyFrame2(None, title="The Main Frame") # создание фрейма на основе нашего класса MyFrame2
      self.SetTopWindow(self.frame) #устанавливаем окно программы сверху остальных окон
      self.frame.Show() # показываем окно
      return True
class MyFrame2(wx.Frame): #Создаем свой класс MyFrame2 на основе класса wx.Frame
  def __init__(self, parent, id=wx.ID_ANY, title="", # Создаем свой конструктор инициализации
      pos=wx.DefaultPosition, size=wx.DefaultSize,
      style=wx.DEFAULT_FRAME_STYLE,
      name="MyFrame"):
        super(MyFrame2, self).__init__(parent, id, title, #инициализация через родительскую инициализацию
                            pos, size, style, name) #   super(в скобках у super первым стоит потомок MyFrame2)

        # Attributes
        self.panel = wx.Panel(self) # Создаем "атрибут класса" - panel self- то что он принадлежит этому классу

        self.panel.SetBackgroundColour(wx.BLACK)
        self.button = wx.Button(self.panel,      # Создаем "атрибут класса" - button- кнопку
                                label="Push Me",
                                pos=(50, 50))

        self.btnId = self.button.GetId()

        # Event Handlers
        self.Bind(wx.EVT_BUTTON, self.OnButton, self.button)

  def OnButton(self, event):

    print("\nFrame GetChildren:")
    for child in self.GetChildren():
        print("%s" % repr(child))
    print("\nPanel FindWindowById:")
    button = self.panel.FindWindowById(self.btnId)
    print("%s" % repr(button))
    print("Button ID: ", button.GetId())
     # Change the Button's label
    button.SetLabel("Changed Label")
    print("\nButton GetParent:")
    panel = button.GetParent()
    print("%s" % repr(panel))
    print("\nGet the Application Object:")
    app = wx.GetApp()
    print("%s" % repr(app))
    print("\nGet the Frame from the App:")
    frame = app.GetTopWindow()
    print("%s" % repr(frame))






if __name__ == "__main__":
 app = MyApp(False)
 app.MainLoop()