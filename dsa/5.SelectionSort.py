# Selection Sort Implementation
# Time Complexity: O(n^2)
# For each pass only one swap is required
def selection_sort(array):
    n = len(array)
    for i in range(n):
        # min takes the index of the minimum value in anarray at each iteration
        min = i
        for j in range(i+1,n):
            if array[min] > array[j]:
                min = j
        # swap array[i] with array[min]
        array[i], array[min] = array[min], array[i] 
    return array

# Driver code
array = [50, 25, 38, 44, 99, 16, 11, 21]
result = selection_sort(array)
print("Selection Sort:", result)

