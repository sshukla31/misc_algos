'''
Given a string, parse it and return a string array. It's like a tokenizer, but the rules are too...

For exmple, string="abc(edf)hij{klmn}opq[rst]uvw"

The delimitors are (), {}, []. They are in pair. So output array:

["abc", "edf", "hij", "klmn", "opq", "rst", "uvw"]

That's the rule 1. The rule 2 is, if any two consecutive "(" means escaping, that is "((" is actually output char "(". It's not part of the delimitor. Similar to ")", "{", "}", "[", "]".

abc(e))df) => ["abc", "e)df"], since the "))" outpus ")".

Rule 3: if "{" is inside a delimitor pair (), then "{" isn't part of the delimitor. Output it as is.

abc(e{df}}g) => ["abc", "e{df}}g"]

So, parse the given string and assume the given string is always valid and parsable.
'''


def tokenize(string):
    stack = []
    braces = {
        '}': '{',
        ')': '(',
        ']': '['
    }


    temp = ''
    result = []
    for char in string:
        if char in braces.values():
            if len(stack) > 0 and char == stack[-1]:
                # append char to the string
                temp = "".join((temp, char))
            else:
                result.append(temp)
                temp = ''
                stack.append(char)
        elif (len(stack) > 0) and (char in braces.keys()):
            if braces[char] == stack[-1]:
                # pop from stack
                # return final string
                stack.remove(stack[-1])
                result.append(temp)
                temp = ''
            else:
                temp = "".join((temp, char)) 
        else:
            temp = "".join((temp, char)) 

    result.append(temp)
    print result


tokenize("abc(edf)hij{klmn}opq[rst]uvw")
tokenize("abc(e))df)")
tokenize("abc(e{df}}g)")
