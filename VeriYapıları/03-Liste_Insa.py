# İcerik :
# 	* liste uretmek
# 	* donguler
# 	* yan etkiler (side effects) : Kodun yazilma amai disinda yaptigi seylere denir.
# 	* lambda fonksiyonu
# 	* map


l = []

for x in range(1, 11):
	l.append(x**2)
print(l)
print(x) # (yan etki) for icindeki degisken gongu disinda da erişilebiliyor
print()


# LAMBDA :
# lambda calculate : fonksiyonel programing kavramı
# amacı : isimsiz bir fonksiyon tanımlamak
# yan etki bırakmaz!
# bir fonksiyonu al listenin bütün elemanlarına uygula
# aşağıdaki for içinde olduğu gibi
squares = list(map(lambda y: y**2, range(1, 11)))
print(squares)
# print(y) # buarada hata verecek. Cunku yukarıda kullanıldıktan sonra bitti. yok artık!
print()

# MAP :
# map(fonksiyon, liste)
# bir fonksiyonu liste üzerinde uygula
# map'in dondurecegi deger bir map objesi oldugunda oturu
# list() ile listeye cevirdik
def f(x):
	return x + 5
l2 = [2, 8, 3]
print(list(map(f,l2)))
print(list(map(lambda x: x+5, l2)))
print()

# baska yazdirma sekli 
l3 = [z**2 for z in range(1, 11)] #bu koseli parantezler bir liste olusacagi anlamina gelir
print(l3)
# print(z) # hata verir. pyhton vesiyonalrına gore hata verebilir veya vermez. Yan etki olarak kalabilir veya kalmaz.
print()

# yukaridakinin modifiyeli hali
# esitlerse listeye eklenmiyor
# ilk for'un ilk elemani icin ikinci for bitene kadar donuyor (iç içe for gibi)
l4 = [(x, y) for x in [1,2,3] for y in [3,1,2] if x != y] # ikili liste yapar 
l5 = [(x, y, z) for x in [1,2,3] for y,z in [(1,2), (2,3), (3,4)] if x != y] # uclu liste yapar 
print(l4)
print(l5)
print()
