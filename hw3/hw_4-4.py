import random
import time

def CountSort(array, k):
	count = 0
	res = [0] * len(array)
	h_array = [0] * (k + 1)
	for i in array:
		h_array[array[i]] +=1
	for l in range(1, len(h_array)):
		while h_array[l] > 0:
			res[count] = l
			h_array[l] -= 1
			count += 1
	return res

search_time = []
time_array = []


for i in range(1, 10000, 100):
	test_array = [random.randint(1,i) for _ in range(10000)]
	for k in range(1,10):
		start_time = time.time()
		res = CountSort(test_array, i)
		res_time = time.time() - start_time
		time_array.append(res_time)
	res_time = sum(time_array) / float(len(time_array))	
	search_time.append(res_time)

print(search_time)

search_time = []
time_array = []

for i in range(1, 10000, 100):
	test_array = [random.randint(1,i) for _ in range(10000)]
	for k in range(1,10):
		start_time = time.time()
		res = sorted(test_array)
		res_time = time.time() - start_time
		time_array.append(res_time)
	res_time = sum(time_array) / float(len(time_array))	
	search_time.append(res_time)

print(search_time)