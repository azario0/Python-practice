"""
Given a sring of lowercase letters in the range ascii[a-z], determine the index of a character that can be removed to make the string a palindrome. there may be more than one solution, but any will do. if the word is already a palindrome or there is no solution, return -1. otherwise, return the index of a character to remove. fuction descript : palindromeIndex has the following params : string s: string to analyze. returns- int : the index of the character to remove or -1.  Constraints: 1<= q <= 20, 1<= length of s <= 10^5 + 5
"""

def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            if s[i+1:i+len(s)-2*i] == s[i+1:i+len(s)-2*i][::-1]:
                return i
            elif s[i:len(s)-i-1] == s[i:len(s)-i-1][::-1]:
                return len(s)-i-1
    return -1
