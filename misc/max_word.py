'''
Apple Interview Question Software Engineer in Tests
given 2 arrays wrds[] , chars[] as an input to a function such that 
wrds[] = [ "abc" , "baa" , "caan" , "an" , "banc" ] 
chars[] = [ "a" , "a" , "n" , "c" , "b"] 
Function should return the longest word from words[] which can be constructed from the chars in chars[] array. 
for above example - "caan" , "banc" should be returned 

Note: Once a character in chars[] array is used, it cant be used again. 
eg: words[] = [ "aat" ] 
characters[] = [ "a" , "t" ] 
then word "aat" can't be constructed, since we've only 1 "a" in chars[].
'''

from collections import Counter

words = [ "abc" , "baa" , "caan" , "an" , "banc" ]
chars = [ "a" , "a" , "n" , "c" , "b"] 

max_len = 0
result = []


def get_hashed(element_list):
    element_count = dict()
    for k, v in Counter(element_list).iteritems():
        element_count.update({k: v})

    return element_count

char_count = get_hashed(element_list=chars)


for word in words:
    word_count = get_hashed(element_list=list(word))

    if len(word_count) > len(char_count) or len(word) < max_len:
        continue

    valid = True
    for k, v in word_count.iteritems():
        if k not in char_count or v > char_count[k]:
            valid = False

    if not valid:
        continue

    if max_len < len(word):
        max_len = len(word)
        result = []
    result.append(word)

print result
