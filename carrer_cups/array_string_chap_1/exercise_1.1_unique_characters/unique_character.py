def get_unique_list(names):
    result = {}
    for val in names:
        result.update({val: True})
        for index, char in enumerate(sorted(val)):
            if index == len(val) - 1:
                break
            elif char == val[index + 1]:
                result.update({val: False})
                break;

    print result


if __name__ == '__main__':
    names = ['aabc', 'abcd', 'abcc', 'abcldefghhikl']
    result = get_unique_list(names)
