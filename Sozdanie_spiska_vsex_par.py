from time import clock, sleep
import time
import json

start1 = clock()


def lst_tupl():  # функция создает список кортежей
	# nambers=f
	lst = []
	squared_odds = [0,0]  # на самом деле это не где девятки, а здесь регулируется длина кортежа
	for k in range(37):
		start1 = clock()
		time.sleep(0.001)
		squared_odds[0] = k
		tp = tuple(squared_odds)
		for s in range(37):
			squared_odds[1] = s
			tp = tuple(squared_odds)
			lst.append(tp)
	
	print(lst)
	return lst


lst_of2 = lst_tupl()
with open('2sh.txt', 'w') as jsonfile: json.dump(lst_of2, jsonfile)
end1 = clock()
print("первая часть(генерация всех 2-ек): выполняется за " + "\nФункция %1.10f секунд" % (end1 - start1))
d = (36,30)
start1 = clock()
z = 0
for i in lst_of2:
	z = z + 1
	if hash(i) == hash(d):
		print('это z', z, "-", i)
	#else:
		#print('не найденно совпадений')
end1 = clock()

print("Вторая часть(поиск сравнений): выполняется за " + "\nФункция %1.10f секунд" % (end1 - start1))
print("длинна-", len(lst_of2))
