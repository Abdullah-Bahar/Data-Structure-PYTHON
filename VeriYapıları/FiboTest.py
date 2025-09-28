"""
	Bir dosyayi import edebilmek icin
	import edilecek dosyanin adina dikkat edilmesi gerek
	harf veya '_' ile baslamali
	bunlar disinda bir isimlendirm ekullanilirsa import etme konusunda bir sorun yasanabilir
"""

import Fibo
import sys	# komut satırında veri okumak icin
			# komut satirinda okunan veriinin string olduğunu unutmamak lazım. Ona göre...

Fibo.fib(int(sys.argv[1]))
print(Fibo.fib2(int(sys.argv[2])))
Fibo.fibIteratif(int(sys.argv[3]))
print(Fibo.fibRecursive(int(sys.argv[4])))