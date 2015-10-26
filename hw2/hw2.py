import random
import time

##################
# Task 1
##################

def binarySearch(array, value):
	if len(array) == 0:
		return False
	else:
		midpoint = len(array)//2
		if array[midpoint] == value:
			return True
		else:
			if value < array[midpoint]:
				return binarySearch(array[:midpoint],value)
			else:
				return binarySearch(array[midpoint + 1:],value)

search_time = []
time_array = []

for i in range(1000, 1000000, 10000):
	test_array = [random.randint(1,500) for _ in range(i)]
	test_array = sorted(test_array)
	for k in range(1,10):
		start_time = time.time()
		res = binarySearch(test_array, 20)
		res_time = time.time() - start_time
		time_array.append(res_time)
	res_time = sum(time_array) / float(len(time_array))	
	search_time.append(res_time)

print(search_time)
