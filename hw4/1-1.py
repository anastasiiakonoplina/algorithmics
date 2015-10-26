# Implement a program that reads input data as in this file and outputs the following:

	# depth of a tree
	# width at each level
	# pre-, in-, and postorder of the tree (node labels)
	# parenthesised version of the tree

#import bintrees 2.0.2

tree_file = open("HW4_1.txt", 'r')
words = tree_file.readlines()
tree = {}
for i in range(2, len(words)):
	tree = words[i].split()

print tree