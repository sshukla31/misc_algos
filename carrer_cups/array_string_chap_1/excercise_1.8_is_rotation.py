def is_rotation(s1, s2):
    if (len(s1) == len(s2) and len(s1) !=0):
        if s2 in "".join((s1,s1)):
            return True

        return False


if __name__ == '__main__':
    print is_rotation("waterbottle", "erbottlewat")
