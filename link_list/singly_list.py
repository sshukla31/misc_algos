class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add_simple(self, data):
        """
        Traverse all node and then add element.
        Not that efficient method
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while(temp.next is not None):
                temp = temp.next

            temp.next = new_node

    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            temp = self.tail
            temp.next = self.tail = new_node


    def print_list(self):
        temp = self.head

        while(temp is not None):
            print temp.data
            temp = temp.next


    def reverse_list(self):
        curr_ptr = self.head
        result = next_ptr = None

        while(curr_ptr is not None):
            next_ptr = curr_ptr.next
            curr_ptr.next = result
            result = curr_ptr
            curr_ptr = next_ptr

        self.head = result


if __name__ == '__main__':
    link_list = LinkList()
    for val in range(0, 5):
        link_list.add(val)

    link_list.print_list()
    link_list.reverse_list()
    print "-----------------"
    link_list.print_list()

