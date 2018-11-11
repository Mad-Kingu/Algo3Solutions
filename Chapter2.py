#Solutions
#Python version 2.7
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
	print "timetest begins"
	
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

#Test results for 100 integer

![Bilby Stampede](https://i.imgur.com/a5f10BA.jpg)
