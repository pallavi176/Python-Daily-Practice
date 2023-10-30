# In this challenge, the user enters a string and a substring. You have to print the number of times that the 
# substring occurs in the given string. String traversal will take place from left to right, not from right to left.

def count_substring(string, sub_string):
    l = len(sub_string)
    tot = 0
    for c in range(len(string) - l + 1):
        if string[c:c+l] == sub_string:
            tot += 1
    return tot

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)