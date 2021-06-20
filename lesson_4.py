import math as m
import random

print('Hello, World!')
def sum_number(a, b):
	return a + b

print(sum_number(5, 7)) #develop 1

a = m.pi * sum_number(2, 4) #develop 2

while a > 0:           # develop 3
	if int(a) % 2 == 0:
		print(a)
	a -= 3

if sum_number(5, 5) > 10:  # issue53 - 1
	print('ok')
else:
	print('no')

print(10 * '-', 'new line', 10 * '-')   # issue53 - 2

b = random.randint(1, 50)    # issue53 - 3
print(b)

print('new branch issue75')  # issue75
