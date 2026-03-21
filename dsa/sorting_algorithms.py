my_list = [6,2,89,3,2,4,64,1,2,4,6,9,5,45]
my_list2 = [5,3,4,1,2]

# bubble sort

def bubble_sort(list_to_sort):
    for i in range(len(list_to_sort)):
        swapped = False
        for j in range(len(list_to_sort)-i-1):
            if list_to_sort[j] > list_to_sort[j+1]:
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
                swapped = True
            print(list_to_sort)
        if not swapped:
            break
        print()


def selection_sort(list_to_sort):
    print(list_to_sort)
    for i in range(0,len(list_to_sort)):
        min_index = i
        print(min_index)
        for j in range(i+1,len(list_to_sort)):
            if list_to_sort[j] < list_to_sort[min_index]:
                min_index = j
        list_to_sort[i], list_to_sort[min_index] = list_to_sort[min_index], list_to_sort[i]
        print(list_to_sort)

def insertion_sort(list_to_sort):
    for i in range(1,len(list_to_sort)):
        key = list_to_sort[i]
        index_before = i-1
        while index_before >= 0 and key < list_to_sort[index_before]:
            list_to_sort[index_before+1] = list_to_sort[index_before]
            index_before -= 1
