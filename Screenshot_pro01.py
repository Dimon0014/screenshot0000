import win32ui, win32gui, win32con, win32api
from time import clock

start1 = clock()
hwnd = win32gui.GetDesktopWindow() # получаем хандл экрана
width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN) # получаем координату CX, самую дальнюю точку экрана
height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN) # получаем координату CY
x = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN) # получаем координату X(начало в данном случае X=0) Определяют координаты левой
                                                          # стороны и вершины виртуального экрана.
                                                          # Виртуальный экран – это ограничительный прямоугольник
                                                          #  всех мониторов дисплея.

y = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN) # получаем координату Y(начало в данном случае Y=0)

hwndDC = win32gui.GetWindowDC(hwnd) #извлекает контекст устройства (DC) по хандлу, для всего окна
mfcDC = win32ui.CreateDCFromHandle(hwndDC) # PyCDC object
saveDC = mfcDC.CreateCompatibleDC()# create a memory based device context

# create a bitmap object
saveBitMap = win32ui.CreateBitmap()# пустой объект
saveBitMap.CreateCompatibleBitmap(mfcDC, width, height) # затем инициализируем его размерами от объекта mfcDC

saveDC.SelectObject(saveBitMap)# обращаемся по адресу в памяти где у нас контекст и даем ему ссылку на saveBitMap
saveDC.BitBlt((0, 0), (width, height), mfcDC, (x, y), win32con.SRCCOPY)# copy the screen into our memory device context

# Можно сохранить полученный битмап в BPM огромных размеров
saveBitMap.SaveBitmapFile(saveDC, 'screenshot.bmp')
end1 = clock()

print("Result (iterativ): выполняется за " + "\nФункция %1.10f секунд" % (end1 - start1))
# --------------------------------------------------------------
# Либо воспользоваться PIL для сохранения в любом другом формате
import PIL.Image

bmpinfo = saveBitMap.GetInfo()
bmpstr = saveBitMap.GetBitmapBits(True)
image = PIL.Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
image.save('screenshot.png', format='png')
# --------------------------------------------------------------

saveDC.DeleteDC()
win32gui.DeleteObject(saveBitMap.GetHandle())