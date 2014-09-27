from Queue import Queue

from binary_tree import BinaryTree

def bst(binary_tree):
    queue = Queue()
    queue.put(binary_tree.root)

    while(not queue.empty()):
        element = queue.get()
        print element.data
        if element.left is not None:
            queue.put(element.left)
        if element.right is not None:
            queue.put(element.right)


if __name__ == '__main__':
    """ Successfull Case """
    binary_tree = BinaryTree()
    for value in [5, 2, 1, 9, 10, 0, 6]:
        binary_tree.insert(value)

    bst(binary_tree)
