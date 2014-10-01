"""
Merge K sorted array algorithm
"""

def merge_list(left, right):
    """
    Merge sorted left and right list. Compare elements of 2 list and sort them
    """
    result = []
    i = 0
    j = 0

    while(i < len(left) or j < len(right)):
        # Case 1: left and right list are non-empty
        if(i < len(left) and j < len(right)):
            if(left[i] <= right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        # Case 2: left list is non-empty
        elif(i < len(left)):
                result.append(left[i])
                i += 1
        # Case 3: right list is non-empty
        elif(j < len(right)):
                result.append(right[j])
                j += 1

    return result


def merge(sorted_elements):
    """
    Process each element, merge and return sorted result 
    """ 
    sort_result = []
    for element in sorted_elements: 
        sort_result = merge_list(sort_result, element)
        
    return sort_result

def test():
    """ Test function """
    sorted_elements = [
    [0, 1, 5, 93],
    [2, 6, 89, 101],
    [-1, 3, 7, 15]
    ]
    expected = [-1, 0, 1, 2, 3, 5, 6, 7, 15, 89, 93, 101]
    assert merge(sorted_elements) == expected

if __name__ == '__main__':
    test()
