import numpy
import mlpy

t1 = [0.54, 0.58, 0.78, 0.89, 0.92, 1.2, 0.1, -2, 0.7, 1.9, 2.7, -0.12, 0.7, 0.2, 1.9]
t2 = [1.4, 1, -0.5, -0.6, 0.23, 0.25, 0.27, 0.21, 0.2, -2.4, -1.7, 0.3, 0.9, 1.7, 1.8, 2.8, 1.2, 0, 0.5, 0.4, 0.9, 1, 0, 2]
t3 = [1, 0.2, -0.2, -0.5, -0.4, -0.3, -0.4, 0.3, 0.35, 0.29, 0.32, 0.5, 0.01, -1.2, -1.8, -1.9, -1.8, -0.5, 1.6, 1.9, 0, 1.2, 1.8]
t4 = [1, 1.2, -2.1, 2.7, -0.1, 0.2, 0.2, 0.19, 2.3]
t5 = [0.9, 0.8, -1.4, -1.1, -1.1, 0.15, 0.18, 0.19, -2.1, 1.5, 3, 2.9, 2.8, 0.4, 0.5, 0.98, 0.1, 1.7]
arrays = [t1, t2, t3, t4, t5]

def compareAll(arrays):
	res = {}
	for i in range(0, len(arrays)):
		for j in range(i + 1, len(arrays)):
			res[i,j] = mlpy.dtw_std(arrays[i], arrays[j], dist_only = True)
	return res


print compareAll(arrays)
print mlpy.dtw_std(t1, t1, dist_only = True)