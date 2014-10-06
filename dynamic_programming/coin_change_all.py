# Coin change problem
# All possible ways to change a coin
# Print minimum coins required to change a coin
# Print minimum number of coins required to change a coin

# This snippet of code is referred from a video by Kris Wright on youtube
# http://www.youtube.com/watch?v=EScqJEEKC10

n = 16
coins = [1, 5, 10, 25]

def change(n, coins_available, coins_so_far):
    if sum(coins_so_far) == n:
        yield coins_so_far
    elif sum(coins_so_far) > n:
        pass
    elif coins_available == []:
        pass
    else:
        for coin in change(n, coins_available[:], coins_so_far+[coins_available[0]]):
            yield coin
        for coin in change(n, coins_available[1:], coins_so_far):
            yield coin


# Print all possible way to change a coin
print [s for s in change(n, coins, [])] 

# Print minimum coins required for a change
print min([s for s in change(n, coins, [])], key=len)

# Print minimum number of coins required to change a coin
print len(min([s for s in change(n, coins, [])], key=len))
