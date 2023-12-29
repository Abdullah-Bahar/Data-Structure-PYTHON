# liste özellikleri kullanılarak stack ve queue olusturulabilir.
# Stack (Yığın)	: Last In, First Out
# Queue (Sıra) 	: First In, First Out

# stack yapısı
l = [1, 2, 3]
l.append(55)
print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)
print()

# queue yapısı
# liste kullanilarak yapildi 
l2 = [44, 55, 66]
l2.append(77)
print(l2.pop(0)) # index'i veriyoz ki ilk eleman silinsin
print(l2)
print()

# queue yapısı
# kutuphane kullanilarak yapildi 
from collections import deque

l3 = deque([11, 23, 45])
print(l3)
l3.append(67)
print(l3.popleft())
print(l3)
print()