def merge_list(left, right):
    """
    Merge left and right list. Compare elements of 2 list and sort them
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


def merge_sort(table):
    """
    Find mid and divide table in 2 parts.
    """ 
    length_table = len(table)
    # Stop Condition
    if (length_table <= 1):
        return table
    else:
        # Divide
        mid = length_table / 2
        # Conquer
        sorted_left = merge_sort(table[: mid])
        sorted_right = merge_sort(table[mid : ])
        # Merge
        return merge_list(sorted_left, sorted_right)



if __name__ == '__main__':
    table = [5, 1, 4, 2, 10, 99, 0]
    print merge_sort(table=table)
