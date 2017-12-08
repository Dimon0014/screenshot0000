from time import clock, sleep
import time
lst=[(1, 2, 3), (1, 2, 4), (1, 2, 3), (1, 2, 5)]
a=(1, 2, 5)
if a in lst:
    print("есть")
   # print(lst.index((1, 2, 3)))

else:
    print("нет")
k=0
for i in lst:
    k =k+1
    if hash(i) == hash(a):
     print(k,"-",i)
first_ten_even = [(i, x, x, i, x) for i, x in enumerate(range(100000))]
#print(first_ten_even)   # [(0, 0), (2, 2), (4, 4), (6, 6), (8, 8)]
start1 = clock()
z=0
d=(99999, 99999, 99999, 99999, 99999)
for i in first_ten_even:
    z =z+1
    if hash(i) == hash(d):
     print(z,"-",i)
end1 = clock()
#print(first_ten_even)
print("Result (iterativ): выполняется за " + "\nФункция %1.10f секунд" % (end1 - start1))

def lst_tupl(): # функция создает список кортежей
    #nambers=f
    lst=[]
    squared_odds = [0,0,0,0,0]
    for k in range(36):
        start1 = clock()
        time.sleep(0.001)
        squared_odds[0]=k
        tp=tuple(squared_odds)
        for s in range(36):

           squared_odds[1] = s
           tp = tuple(squared_odds)
           #lst.append(tp)
           for f in range(36):

               squared_odds[2] = f
               tp = tuple(squared_odds)
               #lst.append(tp)
               for f in range(36):
                   end1 = clock()
                   print("Result (iterativ): выполняется за " + "\nФункция %1.10f секунд" % (end1 - start1))

                   squared_odds[3] = f
                   tp = tuple(squared_odds)
                  # lst.append(tp)
                   for f in range(36):
                       squared_odds[4] = f
                       tp = tuple(squared_odds)
                       lst.append(tp)

    print(lst)
    return lst
w, h = 5, 3  # зададим ширину и высотку матрицы
matrix = [[0 for x in range(w)] for y in range(h)]
print(matrix)
matrix = [tuple([0 for x in range(w)]) for y in range(h)]
print(matrix)   # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

start1 = clock()
lis=lst_tupl()
end1 = clock()
#print(first_ten_even)
print("Result (iterativ): выполняется за " + "\nФункция %1.10f секунд" % (end1 - start1))

d=(36, 36, 36, 36, 36)
start1 = clock()
for i in lis:
    z =z+1
    if hash(i) == hash(d):
     print(z,"-",i)
end1 = clock()
#print(first_ten_even)
print("Result (iterativ): выполняется за " + "\nФункция %1.10f секунд" % (end1 - start1))
print(len(lis))