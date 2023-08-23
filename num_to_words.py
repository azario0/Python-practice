"""
The numbers 1 to 5 written out in words are One, Two, Three, Four, Five

First character of each word will be capital letter for example:
 10438242112 is One Hundred Four Billion Three Hundred Eighty Two Million Four Hundred Twenty One Thousand One Hundred Twelve
 
 Given a number, you have to write it in words.

Input Format

The first line contains an integer T, i.e., number of test cases.
Next  lines will contain an integer N.

Constraints
1 <= T <= 10
0 <= N <= 10^12
"""
# Define a dictionary of words representing the numbers 1 to 10
words = {i: word for i, word in enumerate(["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"])}

# Define a dictionary of words representing the numbers 11 to 19
teens = {i: word for i, word in enumerate(["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"], start=11)}

# Define a dictionary of words representing the tens place of numbers
tens = {i: word for i, word in enumerate(["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"])}

# Define a list of words representing the thousands, millions, billions, and trillions place of numbers
suffixes = ["", "Thousand", "Million", "Billion", "Trillion"]

def num_to_words(n):
    # If the input number is 0, return "Zero"
    if n == 0:
        return "Zero"
    
    # Convert the input number to a string and split it into groups of three digits
    num_str = str(n)
    groups = []
    while num_str:
        groups.append(num_str[-3:])
        num_str = num_str[:-3]
    
    # Convert each group of three digits into its corresponding word representation
    words_list = []
    for i, group in enumerate(groups):
        group_words = []
        group = int(group)
        if group >= 100:
            group_words.append(words[group // 100] + " Hundred")
            group %= 100
        if group >= 11 and group <= 19:
            group_words.append(teens[group])
        elif group == 10 or group >= 20:
            if group % 10 != 0:
                group_words.append(tens[group // 10] + " " + words[group % 10])
            else:
                group_words.append(tens[group // 10])
        elif group >= 1 and group <= 9:
            group_words.append(words[group])
        if group != 0:
            group_words.append(suffixes[i])
        words_list.append(" ".join(group_words))
    
    # Reverse the list of word representations and join them together with spaces
    words_list.reverse()
    return " ".join(words_list)

if __name__ == "__main__":
    # Read the number of test cases from standard input
    t = int(input())
    
    # Loop through each test case
    for i in range(t):
        # Read the input number from standard input
        n = int(input())
        
        # Convert the input number to its corresponding word representation and write it to standard output
        print(num_to_words(n))