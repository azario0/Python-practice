"""
The numbers 1 to 5 written out in words are One, Two, Three, Four, Five

First character of each word will be capital letter for example:
 10438242112 is Given a number, you have to write it in words.

Input Format

The first line contains an integer T, i.e., number of test cases.
Next  lines will contain an integer N.

Constraints
1 <= T <= 10
0 <= N <= 10^12
"""
def num_to_words(N,T,words):
    for i in range(T):
        if N[i] == 0:
            print("Zero")
        else:
            print(words[N[i]])
if __name__ == "__main__":
    T = int(input())
    N = []
    words = {0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",
             7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",
             13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",
             17:"Seventeen",18:"Eighteen",19:"Nineteen",20:"Twenty",
             30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",
             80:"Eighty",90:"Ninety",100:"Hundred",1000:"Thousand",
             100000:"Lakh",10000000:"Crore"}
    for i in range(T):
        N.append(int(input()))
    num_to_words(N,T,words)
    