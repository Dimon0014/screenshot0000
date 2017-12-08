import wx, ctypes
from time import clock
start1 = clock()
app = wx.App()

SM_XVIRTUALSCREEN = 76
SM_YVIRTUALSCREEN = 77
SM_CXVIRTUALSCREEN = 78
SM_CYVIRTUALSCREEN = 79

user32 = ctypes.windll.user32
# узнаем размеры экрана
width, height = user32.GetSystemMetrics(SM_CXVIRTUALSCREEN), user32.GetSystemMetrics(SM_CYVIRTUALSCREEN)
x, y = user32.GetSystemMetrics(SM_XVIRTUALSCREEN), user32.GetSystemMetrics(SM_YVIRTUALSCREEN)

screen = wx.ScreenDC()#A ScreenDC can be used to paint on the screen
bmp = wx.Bitmap(width, height) # конструктор создает битовую матрицу заданых размеров
mem = wx.MemoryDC(bmp) # создаем в памяти контекст отображения(DC)помещаем ссылку на битовую матрицу в контекст памяти
mem.Blit(0, 0, width, height, screen, x, y) # копируем из другого контекста в этот, заполняем ее картинкой из screen
del mem
bmp.SaveFile('screenshot106.bmp', wx.BITMAP_TYPE_BMP)

end1 = clock()

print("Result (iterativ): выполняется за " + "\nФункция %1.10f секунд" % (end1 - start1))