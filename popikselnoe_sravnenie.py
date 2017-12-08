import pyscreenshot as ImageGrab
import os
import time

x_pad=0
y_pad=0
def screenGrab():
	b1 = (x_pad + 1, y_pad + 1, x_pad + 640, y_pad + 480)
	im = ImageGrab.grab(b1)
	
	im.save(os.getcwd() + '\\Sna_pro_'+'.png', 'PNG')
	return im
if __name__ == "__main__" :
 im = screenGrab()
 f_ = (0, 0)
 p=im.getpixel(f_)
 p2=im.getpixel((0, 0))
 if p==p2:
	 print('пикселы равны')
 else:
	 print('пикселы не равны')