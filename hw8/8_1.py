import random

lim = 2**(64 - 1)

numbers = random.sample(range(0, lim), 10100)
numbers1 = numbers[:100]
numbers2 - numbers[101:]

n = 1600
array = [0] * n

functions = [[2,3], [100, 769]]

def hashFunc(key, params):
	return key * params[]

def bloomFilter(numbers, array, functions):
	for num in numbers:
		ones = []
		for i in functions:
			ones.append(hashFunc(num, i))
		for one in ones:
			array[one] = 1
	return array