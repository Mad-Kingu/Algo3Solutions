#Solutions
#Python version 2.7
# 5 Algorithm Tested 

import os
import re
import math
import random
import time

def insertion_sort(array):
	for j, v in enumerate(array):
		key = v
		i = j - 1
		while i > -1 and array[i] > key:
			array[i+1] = array[i]
			i = i - 1
		array[i+1] = key
			
			
def reverse_insertion_sort(array):
	for j, v in enumerate(array):
		key = v
		i = j - 1
		while i > -1 and array[i] < key:
			array[i+1] = array[i]
			i = i - 1
		array[i+1] = key

# 2.3-1 Merge Sort With Sentinel
def merge_sort_with_sentinel(array, p, r):
	if p < r: 
		q = int((p + r)/2) #math int flooring the value
		merge_sort_with_sentinel(array, p, q)
		merge_sort_with_sentinel(array, q+1, r)
		merge_with_sentinel(array, p, q, r)
	
def merge_with_sentinel(array, p, q, r):
	n1 = q - p + 1
	n2 = r - q
	L = [None] * (n1 + 1)
	R = [None] * (n2 + 1)
	for i in range(0, n1):
		L[i] = array[p + i]
	for j in range(0, n2):
		R[j] = array[q + j + 1]
	L[n1] = 1023				#this and
	R[n2] = 1023				#this are the sentinels
	i = 0
	j = 0
 	for k in range(p, r+1):
		if L[i] <= R[j]:
			array[k] = L[i]
			i += 1
		else:
			array[k] = R[j]
			j += 1
		
# 2.3-2 Normal Merge Sort Without Sentinel
def merge_sort(array, p, r):
	if p < r:
		q = int((p + r)/2) #math int flooring the value
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

# 2-3.4 Recursive Insertion Sort
def recursive_insertion_sort(array, p, q):
	if q > 0:
		q = q - 1
		recursive_insertion_sort(array, p, q)
		recursive_insertion_merge(array, p, q)

def recursive_insertion_merge(array, p, q):
	i = 0
	while i < q:
		if array[i+2] < array[i+1] and array[i] < array[i+2]:
			array[i+1], array[i+2] = swap(array[i+1], array[i+2])
			if i > 2:
				i -= 3
			elif i > 1:
				i -= 2
		elif array[i + 2] < array[i]:
			array[i+2], array[i] = swap(array[i+2], array[i])
			if array[i+1] > array[i+2]:
				array[i+1], array[i+2] = swap(array[i+1], array[i+2])
			if i > 2:
				i -= 3
			elif i > 1:
				i -= 2
		elif array[i + 2] > array[i+1]:
			i += 1
			continue
		i += 1
			
def swap(a,b):
	temp = a
	a = b
	b = temp
	return a, b
	
def testcase():
	array = []
	array_range = 100
	for x in range(array_range):
		array.append(random.randint(1, 1000))
	return array

if __name__ == '__main__':
	print "time test begins"
	array1 = testcase()
	
	array = array1
	t0 = time.clock()
	insertion_sort(array)
	t1 = time.clock()
	print "insertion sort: " + str(t1-t0)
	for i, v in enumerate(array):
		print " " + str(v),
	print ""

	array = array1
	t0 = time.clock()
	reverse_insertion_sort(array)
	t1 = time.clock()
	print "reverse insertion sort: " + str(t1-t0)
	for i, v in enumerate(array):
		print " " + str(v),
	print ""

	array = array1	
	t0 = time.clock()
	merge_sort_with_sentinel(array, 0, array.__len__() - 1)
	t1 = time.clock()
	print "merge_sort_with_sentinel: " + str(t1-t0)
	for i, v in enumerate(array):
		print " " + str(v),
	print ""

	array = array1
	t0 = time.clock()
	merge_sort(array, 0, array.__len__() - 1)
	t1 = time.clock()
	print "merge_sort: " + str(t1-t0)
	for i, v in enumerate(array):
		print " " + str(v),
	print ""

	array = array1
	t0 = time.clock()
	recursive_insertion_sort(array, 0, array.__len__() - 1)
	t1 = time.clock()
	print "recursive_insertion_sort: " + str(t1-t0)
	for i, v in enumerate(array):
		print " " + str(v),
	print ""

#Test results for 100 random integer with 1.000 max
#insertion sort:-----------0.000376615075598
#reverse insertion sort:---0.000407794537194
#merge_sort_with_sentinel:-0.000437332974496
#merge_sort:---------------0.000550973906893
#recursive_insertion_sort:-0.00318604866786

#Test results for 1.000 random integer with 1.000.000 max
#insertion sort:-----------0.0470682690722
#reverse insertion sort:---0.0364241752417
#merge_sort_with_sentinel:-0.00485579088756
#merge_sort:---------------0.00696122505746
#recursive_insertion_sort is dead because of python reached maximum resursive number

#Test results for 10.000 random integer with 1.000.000 max
#insertion sort:-----------3.63857834783
#reverse insertion sort:---3.6648724801 (9.xxxxx worst case time which is reversed)
#merge_sort_with_sentinel:-0.054934108772
#merge_sort:---------------0.0771092700642
#recursive_insertion_sort is dead because of python reached maximum resursive number


# Binary Search standalone 
# Exercise 2.3-5 in book
import os
import re
import math
import random
import time

def binary_search(array, searchingelement):
	z = array.__len__()
	sign = 0
	last = z
	mid = int(z/2)
	min = 0
	for i in range(int(math.log(z)/math.log(2)) + 1):
		if array[mid] == searchingelement:
			print str(mid) + " th index"
			sign = 1
			break
		elif array[mid] < searchingelement:
			min = mid
			mid = int((last + mid) / 2)
		elif array[mid] > searchingelement:
			last = mid
			mid = int((mid + min) / 2)
	if sign == 0:
		print "can not find the element"
		
if __name__ == '__main__':
	array = []
	for i in range(1000000):
		array.append(i)
	t0 = time.clock()
	binary_search(array, 345676)
	t1 = time.clock()
	print "binary_search: " + str(t1-t0)
# End of 2.3-5 in book

# Exercise 2.3-6 in book
import os
import re
import math
import time
from random import randint

def insertion_sort(array):
	for j, v in enumerate(array):
		key = v
		i = j - 1
		while i > -1 and array[i] > key:
			array[i+1] = array[i]
			i = i - 1
		array[i+1] = key
		
def insertion_sort_v2(array):
	for j, v in enumerate(array):
		key = v
		if j > 3:
			a = binary_search(array, key, j)
			array.insert(a, key)
			array.pop(a+1)

def binary_search(array, searchingelement, arraypart):
	array = array[:arraypart]
	last = array.__len__()
	mid = int(last/2)
	min = 0
	for i in range(int(math.log(last)/math.log(2)) + 1):
		if array[mid] == searchingelement:
			return mid
		elif array[mid] < searchingelement:
			min = mid
			mid = int((last + mid) / 2)
		else:
			last = mid
			mid = int((mid + min) / 2)
	return mid
	
if __name__ == '__main__':
	array1 = []
	for i in range(1000):
		array1.append(randint(0, 1000))
	
	array = array1
	t0 = time.clock()
	insertion_sort(array)
	t1 = time.clock()
	print "insertion_sort: " + str(t1-t0)
			
	array = array1
	t0 = time.clock()
	insertion_sort_v2(array)
	t1 = time.clock()
	print "insertion_sort_v2: " + str(t1-t0)
# Test results shows that worst case of improved insertion sort is O(n * lg(n)) 
# Tested for 1000 random elements
# insertion_sort:----0.0393522697063
# insertion_sort_v2:-0.00700267815824
# End of 2.3-6 in book





