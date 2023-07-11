# Time complexity: O(n)
def mat_search(mat, search_element):
    i = 0
    j = len(mat[0])-1
    while True:
        if j < 0 or i == len(mat):
            return 0
        elif search_element < mat[i][j]:
            j -= 1
        elif search_element > mat[i][j]:
            i += 1
        else:
            return 1
        
def search2DSortedMatrix(mat, search_element):
    i = 0
    j = len(mat[0])-1 # no of col in a matrix
    n = len(mat)
    # Time complexity: O(n)
    while (i < n and j >= 0):
        if mat[i][j] == search_element:
            return 1
        elif mat[i][j] > search_element:
            j -= 1
        else:
            i += 1
    return 0
    
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
search_element = 5
result = mat_search(matrix, search_element)
print("Search element found", result)

search_element = 11
result = mat_search(matrix, search_element)
print("Search element found", result)

search_element = 190
result = mat_search(matrix, search_element)
print("Search element found", result)

search_element = -190
result = mat_search(matrix, search_element)
print("Search element found", result)

search_element = 5
result = search2DSortedMatrix(matrix, search_element)
print("Search Result is", result)

search_element = 29
result = search2DSortedMatrix(matrix, search_element)
print("Search Result is", result)

search_element = -500
result = search2DSortedMatrix(matrix, search_element)
print("Search Result is", result)

