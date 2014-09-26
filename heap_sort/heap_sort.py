class HeapSort(object):
    def __init__(self, queue):
        self.queue = queue

    def insert(self, val):
        total_size = len(queue) - 1
        index = 0
        while(index < total_size // 2):
            if queue[index] > queue[(2 * index) + 1]:
                print "swapping {}:{}".format(queue[index], queue[(2 * index) + 1])
                queue[(2 * index) + 1], queue[index] = queue[index], queue[(2 * index) + 1]
            elif queue[index] > queue[(2 * index) + 2]:
                print "swapping {}:{}".format(val, queue[(2 * index) + 2])
                queue[(2 * index) + 2], queue[index] = queue[index], queue[(2 * index) + 2]

            index += 1

    #def build_heap(self, queue):








def main():
    #number_list = [10, 1, 4, 2, 7, 6, 9, 0, 3]
    number_list = [1, 2, 3]
    heap = HeapSort(number_list)
    for val in [10, 8, 5, 4, 9]:
        heap.insert(val)
    print number_list


if __name__ == '__main__':
    main()
