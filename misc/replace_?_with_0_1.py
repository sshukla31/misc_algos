name = "Hel???o"

def replace(name):
    char_pos = name.find("?")

    if char_pos == -1:
        return name
    else:
        name_1 = name[:char_pos] + "0" + name[char_pos + 1: ]
        name_2 = name[:char_pos] + "1" + name[char_pos + 1: ]
    
    return [replace(name_1), replace(name_2)]
    
        
print replace(name)
