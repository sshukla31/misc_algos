from binary_tree import (
    BinaryTree,
    Node,
)


def is_bst(node):

    if node is None:
        print "Root is None"
        return False

    if(node.left != None and node.right != None):
        if((node.data > node.left.data) and (node.data < node.right.data)):
            return (is_bst(node.left/Users/Private/Desktop/python_practice/trees/binary_tree/binary_tree.py) and is_bst(node.right))
        else:
            print "node value {} has left child {} and right child {}".format(node.data,
                                                                              node.left.data,
                                                                              node.right.data, )
            return False
    elif(node.left == None and node.right != None):
        if(node.data < node.right.data):
            return (is_bst(node.right))
        else:
            print "node value {} has left child {} and right child {}".format(node.data,
                                                                              node.left.data,
                                                                              node.right.data, )
            return False
    elif(node.left != None and node.right == None):
        if(node.data > node.left.data):
            return (is_bst(node.left))
        else:
            print "node value {} has left child {} and right child {}".format(node.data,
                                                                              node.left.data,
                                                                              node.right.data, )
            return False
    else:
        return True


if __name__ == '__main__':
    """ Successfull Case """
    binary_tree = BinaryTree()
    for value in [5, 2, 1, 9, 10, 0, 6]:
        binary_tree.insert(value)
    if is_bst(binary_tree.root):
        print "its a BST"
    else:
        print "it not a BST"

    """ Root is null case """
    is_bst(None)

    """ Unsuccessful case """
    # Lets construct an invalid tree
    parent_node = Node(5)
    parent_node.left = Node(6)
    parent_node.right = Node(8)
    if is_bst(parent_node):
        print "its a BST"
    else:
        print "it not a BST"

