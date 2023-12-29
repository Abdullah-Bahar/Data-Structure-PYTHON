l = [1,2,3, 1,2,3] # list
t = (4,5,6, 4,5,6) # tuple (kayit)
k = {7,8,9, 7,8,9} # kumeler  	, curly bracket (kume parantezi)
print(l)
print(t)
print(k)
print()

"""
kumeler ve listelerin farki su ki
listelerde ayni elemanda bir kac tane olabilir, kumede olmaz
cunku kumenin genel olarak tanimi su ki her bir eleman a-en fazla bir kere gecmeli
ancak ayni elemandan bir kac tane eklersek hata vermez. Lakin yardirmaya calisirsak tekrar edenleri yazdirmaz.

Ayrica 
	liste -> Ordined (sirali)
	tuple -> Ordered
	kume (set) -> UnOrdered (sirasiz)
"""

# set fonksiyonu bir liste alir ve o listeyi kumeye cevirir
k2 = set(l) # listeyi kumeye cevirdik
k3 = set([10,11,12,10,11,12])
k4 = set(t) # tuple'yi kumeye cevirdik
print(k2)
print(k3)
print(k4)
print()


k5 = set('abdullahbahar')
k6 = set("berkaygumrukcu")
print(k5)
print(k6)
print()


print(k5 | k6) # set union, birlesim islemi
print(k5 - k6) # kume farki
print(k5 & k6) # kesisim
print(k5 ^ k6) # exclusive or, ozel vaya   (ikisinden sadece birinde olanlari alir)
print()

