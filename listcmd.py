"""
Consider a list(list =[]). you can perform the following cmds :
insert i e: insert integer e at position i.
print: print the list.
remove e: delete the first occurrence of integer e.
append e: insert insert e at the end of of the list. 
sort: sort the list. 
pop: pop the last element from the list. 
reverse: reveser the list.
Initiallize your list and read in the value of n followed by lines of commands where each cmds of the 7 types I mentioned above. iterate through each cmd in order and perform the corresponding operation your list. Constraints: the elements added to the list must be integers. Input format: the first line contains an integer, n, denoting the number of cmds. each line i of the n subsequent lines contains one of the cmds described above.
"""
if __name__ == '__main__':
    n = int(input())
    my_list = []
    for i in range(n):
        cmd = input().split()
        if cmd[0] == "insert":
            my_list.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'print':
            print(my_list)
        elif cmd[0] == "remove":
            my_list.remove(int(cmd[1]))
        elif cmd[0] == "append":
            my_list.append(int(cmd[1]))
        elif cmd[0] == "sort":
            my_list.sort()
        elif cmd[0] == "pop":
            my_list.pop()
        elif cmd[0] == "reverse":
            my_list.reverse()