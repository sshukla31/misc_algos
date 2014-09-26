class MergeSort(object):
    def __init__(self, data):
        self.data = data

    def merge_data(self, left, right):
        result = []
        i = j = 0

        while(i < len(left) or j < len(right)):
            if(i < len(left) and j < len(right)):
                if(left[i] <= right[j]):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            elif(i < len(left)) :
                result.append(left[i])
                i += 1
            elif(j < len(right)) :
                result.append(right[j])
                j += 1

        return result

    def sort(self, input_list):
        length = len(input_list)
        if length <= 1:
            return input_list
        else:
            mid = length / 2
            left_list = self.sort(input_list[ : mid])
            right_list = self.sort(input_list[mid : ])
            return self.merge_data(left_list, right_list)


if __name__ == '__main__':
    data = [5, 1, 4, 2, 10, 99, 0]
    merge_sort = MergeSort(data)
    print merge_sort.sort(merge_sort.data)
