a = [range(0, 4), range(4, 8), range(8, 12), range(12, 16)]
n = len(a)

#for i in range(0, n //2):
#    import ipdb;ipdb.set_trace() 
#    for j in range(i, (n - i -1)):
#        tmp = a[i][j]
#        a[i][j]=a[j][n-i-1]
#        a[j][n-i-1]=a[n-i-1][n-j-1]
#        a[n-i-1][n-j-1]=a[n-j-1][i]
#        a[n-j-1][i]=tmp
#

for i in range(0, n/2):
    import ipdb;ipdb.set_trace() 
    for j in range(i, (n - i)):
        print "{}:{}".format(i, j)
        p1 = a[i][j]
        p2 = a[j][n-i-1]
        p3 = a[n-i-1][n-j-1]
        p4 = a[n-j-1][i]

        a[j][n-i-1] = p1
        a[n-i-1][n-j-1] = p2
        a[n-j-1][i] = p3
        a[i][j] = p4
print a
