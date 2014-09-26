'''
def print_spiral_matrix(matrix, rows, columns):
    top = 0
    bottom = rows-1
    left = 0
    right = columns-1
    direction = 0

    while(top<=bottom && left<=right):
        if (direction == 0):
            for value in matrix_list[top]:
                print value
                left+=1
            top+=1
            direction+= 1
        elif (direction == 1):
            for value in 
'''
def spiral(X, Y):
    matrix_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8],]
    x = y = 0
    dx = 0
    dy = -1
    for i in range(max(X, Y)**2):
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
            #print (x, y)
            print matrix_list[x][y]
            # DO STUFF...
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy



if __name__=='__main__':
    matrix_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8],]
    #print_spiral_matrix(matrix=matrix_list, rows=3, columns=3)
    spiral(X=3, Y=3)
