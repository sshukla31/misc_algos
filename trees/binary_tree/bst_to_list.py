class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class LinkData(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.total = 0


    def insert(self, data):
        new_l_node = LinkData(data)
        if self.head is None:
            self.head = self.tail = new_l_node
        else:
            self.tail.next = new_l_node
            new_l_node.previous = self.tail
            self.tail = new_l_node

    def print_list(self):
        temp = self.head
        while(temp is not None):
            print temp.data
            temp = temp.next

class BST(object):
    def __init__(self):
        self.root = None
        self.sorted_list = LinkedList()

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            node = self.root
            while(node is not None):
                if data <= node.data:
                    if node.left is None:
                        node.left = new_node
                        node = new_node
                    node = node.left
                else:
                    if node.right is None:
                        node.right = new_node
                        node = new_node
                    node = node.right


    def print_inorder(self, node=None):
        """ Print tree in-order """
        if node is not None:
            self.print_inorder(node.left)
            print node.data
            self.print_inorder(node.right)

    def binary_to_sorted_list(self, root):
        if root is None:
            return
        else:
            self.binary_to_sorted_list(root.left)
            self.sorted_list.insert(root.data)
            self.binary_to_sorted_list(root.right)


if __name__ == '__main__':

    # Below commented line works
    '''
    Insert, print and purge test
    '''
    binary_tree = BST()
    for value in [5, 2, 1, 9, 10, 0, 6]:
        binary_tree.insert(value)
    #binary_tree.print_inorder(binary_tree.root)
    binary_tree.binary_to_sorted_list(binary_tree.root)  # Insert into list
    binary_tree.sorted_list.print_list()

    print "\n####LinkList####\n"

    link_list = LinkedList()
    for value in [5, 2, 1, 9, 10, 0, 6]:
        link_list.insert(value)
    link_list.print_list()

