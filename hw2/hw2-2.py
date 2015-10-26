import random
test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def dualQuickSort(array):
	if len(array) > 2:
		a = random.sample(array,2)	
		p1 = min(a)
		p2 = max(a)
		part1 = [i for i in array if i <= p1]
		part2 = [i for i in array if ((i > p1) & (i < p2))]
		part3 = [i for i in array if i >= p2]
		part1 = dualQuickSort(part1)
		part2 = dualQuickSort(part2)
		part3 = dualQuickSort(part3)
	else:
		return array
	res = part1 + part2 + part3
	return res


print(dualQuickSort(test))