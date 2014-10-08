#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Coin Flipping and Die Rolls Algorithm

Solution
    Flip the coin three times and use the three coin flips as the bits of a 
    three bit number. If the number is in the range 1 to 6, output the number.  
    Otherwise repeat.
"""

import random

# Generate random number between 1 and 2
toss = lambda: random.randint(1, 2)


def coin():
    """ Return dice value between 1 and 6 using toss function """
    done = True
    number = 0
    while done:
        # We do -1 as we want to get binary value 0 or 1
        bit1 = toss() - 1
        bit2 = toss() - 1
        bit3 = toss() - 1
        
        number = bit1 * 4 + bit2 * 2 + bit3
        # We validate aginst 5 becasue we peform +1 addition while return.
        # If we validate with six, there is probability to return zero
        # which is invalid for a dice
        if number <= 5:
            done = False
    
    # we do +1, as dice's minimum value is 1. It shouldn't return 0
    return number + 1


def optimized_coin():
    """ Return dice value between 1 and 6 using toss function """
    done = True
    number = 0
    bit1 = toss() - 1
    
    while done:
        # We do -1 as we want to get binary value 0 or 1
        bit2 = toss() - 1
        bit3 = toss() - 1
        
        number = bit1 * 4 + bit2 * 2 + bit3
        # We validate aginst 5 becasue we peform +1 addition while return.
        # If we validate with six, there is probability to return zero
        # which is invalid for a dice
        if number <= 5:
            done = False
        else:
            bit1 = bit3
    
    # we do +1, as dice's minimum value is 1. It shouldn't return 0
    return number + 1

print optimized_coin()
