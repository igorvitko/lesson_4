import math as m

print('Hello, World!')
def sum_number(a, b):
	return a + b

print(sum_number(5, 7)) #develop 1

a = m.pi * sum_number(2, 4) #develop 2

while a > 0:           # develop 3
	if int(a) % 2 == 0:
		print(a)
	a -= 3
