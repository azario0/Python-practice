"""
This code uses the input function to prompt the user to enter two numbers,
 which are then converted to integers using the int function and stored in the variables a and b. 
 The find_gcf function is then called with a and b as arguments to find their GCF. 
 Finally, the code prints out a message that includes the original numbers and their GCF.
"""

def find_gcf(a, b):
    if b == 0:
        return a
    else:
        return find_gcf(b, a % b)
    
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

gcf = find_gcf(a, b)

print("The greatest common factor of", a, "and", b, "is", gcf, ".")