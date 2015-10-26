###################################
# Question 1
###################################

import random
lim = 2**64 - 1
array = [random.randint(1, lim) for _ in range(10000)]

res = sorted(array)

