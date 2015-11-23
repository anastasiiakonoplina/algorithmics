import math

cities16 = []
f = open('16.txt','r')
for text in f:
	line = text.strip().split(' ')
	if line != ['']:
		cities16.append(map(int, line))

cities100 = []
f = open('100.txt','r')
for text in f:
	line = text.strip().split(' ')
	if line != ['']:
		cities100.append(map(int, line))

cities1000 = []
f = open('1000.txt','r')
for text in f:
	line = text.strip().split(' ')
	if line != ['']:
		cities1000.append(map(int, line))


def nn(cities, visited, city):
	visited.append(city)
	cities.remove(city)
	distance = []
	if len(cities) > 0:
		for c in cities:
			distance.append(math.sqrt(abs(c[0] - city[0])**2 + abs(c[1] - city[1])**2))
		city = cities[distance.index(min(distance))]
		nn(cities, visited, city)
	else:
		print visited

print nn(cities16, [], cities16[0])
print nn(cities100, [], cities100[0])
print nn(cities1000, [], cities1000[0])

