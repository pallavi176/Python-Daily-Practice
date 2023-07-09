# Time complexity: O(log n)
def binary_search(arr, search_element, n):
	s = 0
	e = n
	for i in range(s, e):
		m = (s + e) // 2
		if arr[i] > search_element:
			e = m
		elif arr[i] < search_element:
			s = m
		else:
			return i
	return -1

# Implementation of Binary Search Algorithm using Recursion Technique
def binarySearch(array, i, j, x):
	# Single element search
	if i == j:
		if array[i] == x:
			return i
		else:
			return -1
	else:
		mid = i + (j-i) // 2
		if array[mid] == x:
			return mid
		elif array[mid] < x:
			# Recursive call
			return binarySearch(array, mid + 1, j, x)
		else:
			# Recursive call
			return binarySearch(array, i, mid - 1, x)
		

arr = [5, 10, 20, 27, 30, 35, 39, 42]
search_element = 27
n = len(arr)
result = binary_search(arr, search_element, n)
print("Search element index is", result)

search_element = 39
result = binary_search(arr, search_element, n)
print("Search element index is", result)

array = [10, 23, 35, 67, 75, 86, 90]
i = 0
j = len(array) - 1
x = 86
result = binarySearch(array, i, j, x)
print("Searching value is present at index", result)

x = 87
result = binarySearch(array, i, j, x)
print("Searching value is present at index", result)