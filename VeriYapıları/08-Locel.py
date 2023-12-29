"""
	Degiskenlerin gecerlilik alani
    
    * Her degisken tanimli oldugu scope icinde gecerlidir.
    

	* local degiskenler 	-> 	Bu değişkenler, yalnızca o fonksiyonun içinde geçerlidir. 
								Fonksiyondan çıktıktan sonra, local değişkenler artık geçerli değildir.
	* global degiskenler 	-> 	Bir fonksiyonun dışında tanımlanan değişkenlerdir. Bu değişkenler, programın her yerinde geçerlidir.
	* nonlocal degiskenler 	->	Bir fonksiyonun içinde tanımlanan, ancak en yakın çevreleyen kapsamda da geçerli olan değişkenlerdir. 
								Bu değişkenler, yalnızca iç içe fonksiyonlarda kullanılır.	

								
"""



def scope_test():
	def do_local():
		spam = "local spam"

	def do_nonlocal():
		nonlocal spam
		spam = "nonlocal spam"

	def do_global():
		global spam
		spam = "global spam"

	spam = "test spam"
	do_local()
	print("After local assignment:", spam)
	do_nonlocal()
	print("After nonlocal assignment:", spam)
	do_global()
	print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

