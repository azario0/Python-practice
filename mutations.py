"""
Python Mutations Problem::

This code defines a function mutate_string that takes a string, a position, and a character as input. It converts the string to a list of characters, replaces the character at the specified position with the given character, and then joins the characters back into a string. The modified string is returned.

In the main block, it reads the original string s, the position i, and the character c from the user's input. It converts i to an integer and then calls the mutate_string function with the provided inputs. The resulting string is then printed.

"""
def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    new_string = ''.join(string_list)
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    i = int(i)
    result = mutate_string(s, i, c)
    print(result)
