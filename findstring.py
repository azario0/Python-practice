"""
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.
"""
def count_substring(string, sub_string):
    #initialize a count for the number of times the substring appears
    count = 0
    #loop through the string, starting at each index
    for i in range(len(string)):
        #if the substring is found at this index, add 1 to the count
        if string[i:].startswith(sub_string):
            count+=1
    #return the final count
    return count

if __name__ == '__main__':
    #get the string from the user
    string = input().strip()
    #get the substring from the user
    sub_string = input().strip()
    
    #call the function and store the result
    count = count_substring(string, sub_string)
    #print the result
    print(count)