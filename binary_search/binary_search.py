def binary_search(number_list, value):
    top = 0
    bottom = len(number_list) - 1
    found = False

    while(top <= bottom) and (found is False):
        middle = (top + bottom) / 2

        if(value == number_list[middle]) :
            found = True
        elif(value < number_list[middle]):
            bottom = middle - 1
        elif(value > number_list[middle]):
            top = middle + 1

    print "Present" if found else "Not Found"




def main():
    array = range(0, 51)
    try:
        value = int(input("No to search for?"))
    except NameError:
        raise "Invlid input foramt"

    binary_search(number_list=array, value=value)

if __name__ == '__main__':
    main()
