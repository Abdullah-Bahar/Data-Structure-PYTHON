l = [1,2,3] # list
t = (4,5,6) # tuple
print(l)
print(t)
print()

"""
list ve tuple arasındaki fark şu ki
liste'nin elemanları değiştirilebilirken tuple değiştirilemez
ancak tuple, yeniden insa edilebilir
* liste -> MUTABLE'dir		(DEGİSTİRİLEBİLİR)
* tuple -> İMMUTABLE'dir 	(DEGİSTİRİLEMEZ)
"""

l[2] = 10
#t[2] = 10 	# hata verecektir

x,y,z = t # tuple'daki değerler x,y,z degiskenlerine kopyalanir. Ancak value kopyalnir, referans değil. 
print(x,y,z)
x = 10
print(x,y,z)
print(t)

t = (x,y,z) # tuple, yeniden insa edildi. (x,y,z degerlerin sahiip hafızada yeni bir tuple oluşturuldu)
print(t)
print()


v = ([1,2,3], [4,5,6]) # tuple'in elemanlari listedir. Dolayısıyla elemanlarina liste muamelesi yapilabilir.
print(v)
v[0][1] = 99  # bu kod hata vermez, calisir. Cünkü degisikli tuple'in elemani olan liste'de yapıyoruz.
print(v)
#v[0] = [10,11,12] # bu kod hata verir. Cünkü degisikligi tuple'de yapmaya calisiyoruz
print()


# tuple'ler parantez kullanilmadan da tanimlanabilir.
tp = 1,2,3
print(tp)


