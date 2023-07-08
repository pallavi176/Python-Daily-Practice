# Time complexity: O(n)
def linearSearch(arr, search_element, n):
	for i in range(n):
		if arr[i] == search_element:
			return i
	return -1

arr = [53, 12, 32, 17, 39, 90]
search_element = 12
n = len(arr)
result = linearSearch(arr, search_element, n)
print("Search element index is", result)

search_element = 93
result = linearSearch(arr, search_element, n)
print("Search element index is", result)

search_element = 17
result = linearSearch(arr, search_element, n)
print("Search element index is", result)