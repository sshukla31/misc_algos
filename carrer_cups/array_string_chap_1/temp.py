#array = [[1, 2], [3, 4]]
array = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

for i in range(0, len(array) // 2):
    no_of_rows = len(array) - 1
    no_of_cols = len(array) - 1 - i
    for j in range(0, no_of_cols):
        tmp = array[i][j]
        #print array
        array[i][j] = array[(no_of_rows) - i][j]
        #print array
        array[(no_of_rows) - i][j] = array[(no_of_rows) - i][no_of_cols - j]
        #print array
        array[(no_of_rows) - i][no_of_cols - j] = array[i][no_of_cols - j]
        #print array
        array[i][(no_of_rows) - j] = tmp
        #print array

print array
