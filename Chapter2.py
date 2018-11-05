#Solutions
#Python version 2.7
#Every code between start and end tag works standalone
#Some of the test cases are very simple because of my lazyness

# Start Simple Insertion Sort
import os
import re
import math

def insertion_sort(array):
	for j, v in enumerate(array):
		key = v
		i = j - 1
		while i > 0 and array[i] > key:
			array[i+1] = array[i]
			i = i - 1
		array[i+1] = key
		
	for v in enumerate(array):
		print v
    
    
if __name__ == '__main__':
	insertion_sort([2,3,7,5])
# End of Simple Insertion Sort

# Start Reversed Insertion Sort
import os
import re
import math
def reverse_insertion_sort(array):
	for j, v in enumerate(array):
		key = v
		i = j - 1
		while i > -1 and array[i] < key:
			array[i+1] = array[i]
			i = i - 1
		array[i+1] = key
		
	for v in enumerate(array):
		print v
    
    
if __name__ == '__main__':
	reverse_insertion_sort([2,3,7,5])
# End of Reversed Insertion Sort

# Start Merge Sort
import os
import re
import math
import random

def merge_sort(array, p, r):
	if p < r: 
		q = int((p + r)/2) #math int flooring the value
		merge_sort(array, p, q)
		merge_sort(array, q+1, r)
		merge(array, p, q, r)
	
def merge(array, p, q, r):
	n1 = q - p + 1
	n2 = r - q
	L = [None] * (n1 + 1)
	R = [None] * (n2 + 1)
	for i in range(0, n1):
		L[i] = array[p + i]
	for j in range(0, n2):
		R[j] = array[q + j + 1]
	L[n1] = 1023
	R[n2] = 1023
	i = 0
	j = 0
 	for k in range(p, r+1):
		if L[i] <= R[j]:
			array[k] = L[i]
			i += 1
		else:
			array[k] = R[j]
			j += 1

if __name__ == '__main__':
	array = []
	array_range = 100
	for x in range(array_range):
		array.append(random.randint(1, 1000)) # just for random samples from random generation
	for i, v in enumerate(array):		      # for bigger number, highest value must be changed
		print str(i) + " " + str(v)
# End of Merge Sort

# Exercise 2.3-2 
# Start of Merge Sort Without Sentinels
import os
import re
import math
import random
def merge_sort(array, p, r):
	if p < r:
		q = int((p + r)/2) #math int flooring the value
		print ("p: %s q:%s r:%s" % (p, q, r))
		merge_sort(array, p, q)
		merge_sort(array, q+1, r)
		merge(array, p, q, r)

def merge(array, p, q, r):
	n1 = q - p + 1
	n2 = r - q
	L = [None] * (n1)
	R = [None] * (n2)
	for i in range(0, n1):
		L[i] = array[p + i]
	for j in range(0, n2):
		R[j] = array[q + j + 1]
	i = 0
	j = 0
	for k in range(p, r+1):
		if len(L) > i and len(R) > j:
			if L[i] <= R[j]:
				array[k] = L[i]
				i += 1
			else:
				array[k] = R[j]
				j += 1
		elif len(L) > i:
			array[k] = L[i]
			i += 1
		elif len(R) > j:
			array[k] = R[j]
			j += 1

def testcase():
	array = []
	array_range = 100
	for x in range(array_range):
		array.append(random.randint(1, 1000))
	return array

if __name__ == '__main__':
	array = testcase()
	merge_sort(array, 0, array.__len__() - 1)
	for i, v in enumerate(array):
		print str(i) + " " + str(v)
# End of Merge Sort Without Sentinels

