"""
Dictionary'deki ilisli 
key - value iliskisi (k-v)
dizilerde -> index (key) - indexte bulunan deger (value)

Sozlukler ozel, bir dizi yapisidir. 
Elemanlarina erismek icin index degil de dizi tanimlamasinda belirttigimiz key ile erisiriz
"""


l = [11,12,13,14,15]
print(l[0])

tel = {"Abdullah" : 1111, "Berkay" : 2222}
print(tel["Abdullah"])

tel["Abdullah"]	= 3333 	# eleman degeri degistirme
print(tel["Abdullah"])

tel["mustafa"] = 4444	# yeni eleman ekleme
print(tel["mustafa"])
print()

# dict ile iki farkli sekilde sozluk tanimlamasi
d1 = dict( {"a": 1, "b": 2, "c": 3} )
d2 = dict( [ ("c", 4), ("d", 5), ("f", 6) ] )
print(d1["a"])
print(d2["c"])
print()


print(d2)
for key, value in d2.items():
	print(key, value)

