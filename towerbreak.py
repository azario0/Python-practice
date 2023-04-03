"""
Two players are a playing a game of Tower Breakers! Player 1 always moves first, and both players always optimally. 
Given the values of n and m, determine which player will win. 
If the first player wins, return 1. otherwise, return 2.
Function description: towerBreaker has the following param(s): 
int n: the number of towers. 
int m: height of each tower.
returns : int: the winnger of the game. 
Constraints :
1 <= t <= 100, 
1 <= n,m<= 10^6
Rules:
1 Initially there are n towers. 2 Each tower is of height m. 3 the players move in alternating turns. 4 in each turn, a player can choose a tower of height x and reduce its height to y, where 1 <= y < x and y `evenly divides` x. 5 if the current player is unable to make a move they lose the game.
"""
def towerBreaker(n, m):
    # check if there are an even number of towers or if the towers have height 1
    if n % 2 == 0 or m == 1:
        return 2
    else:
        return 1
