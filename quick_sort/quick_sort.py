def quick_sort(table, left, right):
    i = left
    j = right
    pivot = table[(left + right) / 2]

    while(i <= j):
        # Case 1: Keep incrementing left index 'i' until i > mid
        while(table[i] < pivot):
            i += 1
        # Case 2: Keep decrementing right index 'j' until j < mid
        while(pivot < table[j]):
            j -= 1

        # Compare value and swap
        if(i <= j):
            tmp = table[i]
            table[i] = table[j]
            table[j] = tmp
            i += 1
            j -= 1

    # Case 3: when j < i
    if (left < j):
        quick_sort(table, left, j)
    if (i < right):
        quick_sort(table, i, right)

    return table

if __name__ == '__main__':
    table = [5, 1, 4, 2, 10, 99, 0]
    quick_sort(table, 0, len(table) - 1)
    print table
