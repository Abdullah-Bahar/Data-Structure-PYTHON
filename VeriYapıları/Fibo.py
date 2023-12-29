# Fibotest.py dosyası tarafından import edilmiştir

def fib(n):
	a = 0
	b = 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()


def fib2(n):
	result = []
	a = 0
	b = 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result


def fibRecursive(n):
    if (n == 1 or n == 2 or n == 1):
        return 1
    return fibRecursive(n - 1) + fibRecursive(n - 2)
	

def fibIteratif(n):
	a = 0	
	b = 1
	while(n >= 0):
		print(a, end=" ")
		temp = a
		a = b
		b = b + temp
		n -= 1
	print()
