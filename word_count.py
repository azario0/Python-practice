"""
You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Constraints:
1 <= n <= 10^5
The sum of the lengths of all the words do not exceed 10^6
All the words are composed of lowercase English letters only.

Input Format

The first line contains the integer, n.
The next n lines each contain a word
"""
def word_count():
    n = int(input())
    words = []
    for i in range(n):
        words.append(input())
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    print(len(word_dict))
    for word in word_dict:
        print(word_dict[word], end=" ")

if __name__ == "__main__":
    word_count()