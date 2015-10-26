import random
import time

def quickSelect(array, k):
    p = array[(len(array) // 2)]
    part1 = [i for i in array if i < p]
    part2 = [i for i in array if i > p]
    p1 = len(part1)
    r = len(array) - len(part1) - len(part2)
    if k >= p1 and k < p1 + r:
        return p
    elif p1 > k:
        return quickSelect(part1, k)
    else:
        return quickSelect(part2, k - p1 - r)

search_time = []
time_array = []

for i in range(1000, 1000000, 10000):
    test_array = [random.randint(1,500) for _ in range(i)]
    for k in range(1,10):
        start_time = time.time()
        res = quickSelect(test_array, 20)
        res_time = time.time() - start_time
        time_array.append(res_time)
    res_time = sum(time_array) / float(len(time_array)) 
    search_time.append(res_time)

print(search_time)