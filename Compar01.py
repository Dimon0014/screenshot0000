import hashlib
tp1=(1, 2, 3, 4)
tp2=(0, 2, 3, 4)
h1=hash(tp1)
h2=hash(tp2)
if h1==h2:
    print("равны")
else:
    print("не равны")
