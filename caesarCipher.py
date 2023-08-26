"""
Julius Caesar protected his confidential information by encrypting it using cipher. Caesar's cipher shifts each letter by number of ltters. if the shift takes you past the end of the alphabet , just rotate back to the front of the alphabet in the case of a rotation by 3,w,x,y, and z would map to z,a,b and c
. `Note` : the cipher only encrypts letters, symbols, such as '-'. remain unecrypted. Function description: caesarCipher has the following params: string s: cleartext. int k: the alphabet rotation factor. returns: string: the encrypted string.  Constraints : 1<= n <= 100, 0<=k <=100. s is a valid ASCII string without any spaces.
"""
def caesarCipher(s, k):
    encrypted = ""
    for c in s:
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            offset = (ord(c) - base + k) % 26
            encrypted += chr(base + offset)
        else:
            encrypted += c
    return encrypted
print('Welcome to Julius Caesar encription .')
input_string = input("Enter the text that you want to encript : ")
shift_amount = int(input("Enter the shift amount: "))
    
encrypted_result = caesarCipher(input_string, shift_amount)
print("Encrypted text:", encrypted_result)