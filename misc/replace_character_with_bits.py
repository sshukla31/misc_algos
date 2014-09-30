""" Replace ? operator with 0 and 1
eg: if input is "tes?t"  //  [tes0t, tes1t]
    "test??"  // [test00, test01, test11, test10]

order of output is irrelevant
"""


def replace(name):
    char_pos = name.find("?")

    if char_pos == -1:
        return name
    else:
        name_1 = name[:char_pos] + "0" + name[char_pos + 1: ]
        output_1 = replace(name_1)
        if output_1 is not None:
            result.append(output_1)
        name_2 = name[:char_pos] + "1" + name[char_pos + 1: ]
        output_2 = replace(name_2)
        if output_2 is not None:
            result.append(output_2)
   
        
result = []
name = "Hel???o"
replace(name)
print result

result = []
name = "Hel?o"
replace(name)
print result
