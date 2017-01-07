'''
A Tree
                    A      |    X
                 /     \   |      \
               B        C  |        Y
             /   \     /   |
           D       E  F    |
         / | \             |
        G  H  I            |
      /                    |
    J                      |
'''



class Node(object):
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

    def __repr__(self):
        return '<Node:%s>' % self.value


def lca(left, right):
    '''Find the lowest common ancestor of two nodes
    Given two Node objects, return the first common parent, or None
    if the nodes have no parents in common.
    Examples using tree above:
        Given nodes B and C, return node A
        Given nodes J and E, return node B
    '''
    # raise NotImplementedError('Your code here!')
    # is_not_root = True
    child_parent_map = {}
    if any([left is None, right is None]):
        return None

    if left == right:
        return left

    while(left is not None):
        child_parent_map[left] = left.parent
        left = left.parent

    is_not_present = True
    while(is_not_present):
        if right == None:
            is_not_present = False

        #if right in child_parent_map:
        #    return right

        if right in child_parent_map:
            is_not_present = False
            print "Common Ancestor: {}".format(right.parent)
            return right
        else:
            if right.parent is None:
                return None
            right = right.parent


    print "No Common Ancestor"
    return None



    # testing code
    # tree 1
nodeX = Node('X', None)
nodeY = Node('Y', nodeX)

# tree 2
nodeA = Node('A', None)

nodeB = Node('B', nodeA)
nodeC = Node('C', nodeA)

nodeD = Node('D', nodeB)
nodeE = Node('E', nodeB)
nodeF = Node('F', nodeC)

nodeG = Node('G', nodeD)
nodeH = Node('H', nodeD)
nodeI = Node('I', nodeD)

nodeJ = Node('J', nodeG)


assertions = (
    # simple case
    (nodeB, nodeC, nodeA),
    (nodeB, nodeB, nodeB),

    # parent contains
    (nodeD, nodeG, nodeD),
    (nodeG, nodeD, nodeD),
    (nodeD, nodeI, nodeD),

    # errors
    (nodeA, None, None),
    (None, nodeA, None),

    # no lca
    (nodeY, nodeB, None),
    (nodeA, nodeX, None),

    # misc tests
    (nodeJ, nodeE, nodeB),
    (nodeA, nodeJ, nodeA),
)

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'
PASS = GREEN + '✓ ' + RESET
FAIL = RED + 'x ' + RESET

errors = 0
for left, right, expected in assertions:
    call = 'lca(%r, %r)' % (left, right)
    try:
        actual = lca(left, right)
    except Exception as e:
        print FAIL + '%s = %r (expected %s)' % (call, e, expected)
        errors += 1
        continue

    if expected is actual:
        print PASS + '%s = %s' % (call, actual)
    else:
        print FAIL + '%s = %s (expected %s)' % (call, actual, expected)
        errors += 1