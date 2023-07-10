# Brute force approach
# Time complexity: O(n^2)
def searching(arr, search_element):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == search_element:
                return 1
    return 0

def searching2(arr, search_element):
    flat_arr = [element for sublist in arr for element in sublist]
    for i in range(len(flat_arr)):
        if flat_arr[i] == search_element:
            return 1
    return 0

array = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
search_element = 12
result = searching(array, search_element)
print("Search element index is", result)

search_element = 11
result = searching(array, search_element)
print("Search element index is", result)

search_element = 19
result = searching(array, search_element)
print("Search element index is", result)

search_element = 11
result = searching2(array, search_element)
print("Search element index is", result)

search_element = 19
result = searching2(array, search_element)
print("Search element index is", result)