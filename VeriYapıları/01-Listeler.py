l = [1,2,3,4]
print(l)

l.append(55) # listenin sonuna ekler
print(l)

l.insert(2, 111) # araya ekler (2. index'e 111 ekler)
l.append(111)
print(l)

l.remove(111) # ilk buldugunu siler
print(l)

print(l.pop()) # sondan bir eleman siler
print(l)

print(l.index(55)) # sayısının kacinci index'te oldugunu söyler

l.append(1)
print(l.count(1))	# '1' elemanından kac tane oldugunu dondurur

l2 = [3, 4, 2]
l.extend(l2)	# listeleri birlestirir
print(l)

l3 = [10, 11, 12]
l.append(l3)	# listeyi append ile eklersek l3, l'nin altında bir liste olur
print(l)		# liste içinde liste olmuş oldu

l.clear()		# listeyi temizler
print(l)

l.sort() # listeyi sıralar (liste icinde liste varsa hata verir)
print(l)

# Liste Kopyalma :
# 	* Shallow Copy 	-> Referansı kopyalar
#	* Deep Copy		-> Objeyi kopyalar
l2 = l3		# l3'e l2'yi kopyalar (refransı kopyalanır. bellekte tek bir yer var)
print(l2)
l2.append(600)	# l2'ye eklendiginde l3'e de eklenmis oldu (Çünkü hafızada aynı yeri gosteriyorlar)
print(l2)
print(l3)

l4 = l2.copy()  # referans değil hafızadaki obje kopyalanır
l4.append(700)	# birinde yapılan degisiklik digerini etkilmez
print(l2)
print(l4)


