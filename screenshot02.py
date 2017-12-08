import win32api, win32con, time


def click(x, y):
	win32api.SetCursorPos((x, y))
	time.sleep(.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
	time.sleep(.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


data = [
	
	(1589, 122),  # 1. Иконка игры
	(1813, 228),  # 2. Ввод пароля
	(1782, 277),  # 3. Закрытие подменю
	(1803, 379),  # 4. Запуск игры
	(1027, 541),  # 5. castle up repair
	(1065, 726),  # 6. ok
	(1773, 299),  # 7. accept
	(1487, 61)  # 8. change village

]
