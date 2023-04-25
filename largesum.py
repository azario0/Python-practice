

###lARGE suM
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())
total_sum = 0
for i in range(n):
    number = int(input().strip())
    total_sum += number
print(str(total_sum)[:10])
