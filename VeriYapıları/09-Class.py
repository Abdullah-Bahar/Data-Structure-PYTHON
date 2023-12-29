class Araba:
	
	hiz = 0
	renk = ""
	tekerSayisi = 4

	def hizlanma(self):
		self.hiz = self.hiz + 1


x = Araba()
x.hiz = 100
x.hizlanma()
print("hiz", x.hiz)