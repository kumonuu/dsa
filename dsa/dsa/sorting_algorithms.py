import time

my_list = [6,2,89,3,2,4,64,1,2,4,6,9,5,45]
my_list2 = [5,3,4,1,2]

# bubble sort

def bubble_sort(list_to_sort):
    comparisons = 0
    swaps = 0
    #print(list_to_sort)
    for i in range(len(list_to_sort)):
        swapped = False
        for j in range(len(list_to_sort)-i-1):
            comparisons += 1
            if list_to_sort[j] > list_to_sort[j+1]:
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
                swaps += 1
                swapped = True
            #print(list_to_sort)
        if not swapped:
            break
        #print()
    print(f"Comparisons for bubble sort: {comparisons}")
    print(f"Swaps for bubble sort: {swaps}")

def selection_sort(list_to_sort):
    comparisons = 0
    swaps = 0
    #print(list_to_sort)
    for i in range(0,len(list_to_sort)):
        min_index = i
        #print(min_index)
        for j in range(i+1,len(list_to_sort)):
            comparisons += 1
            if list_to_sort[j] < list_to_sort[min_index]:
                min_index = j
        list_to_sort[i], list_to_sort[min_index] = list_to_sort[min_index], list_to_sort[i]
        swaps += 1
    #print(list_to_sort)
    print(f"Comparisons for selection sort: {comparisons}")
    print(f"Swaps for selection sort: {swaps}")

def insertion_sort(list_to_sort):
    comparisons = 0
    swaps = 0
    #print(list_to_sort)
    for i in range(1,len(list_to_sort)):
        key = list_to_sort[i]
        index_before = i-1
        #print(key, list_to_sort[index_before])
        while index_before >= 0:
            comparisons += 1
            if key < list_to_sort[index_before]:
                #print("debug")
                list_to_sort[index_before+1] = list_to_sort[index_before]
                swaps += 1
                index_before -= 1
            else:
                break
        list_to_sort[index_before+1] = key
    #print(list_to_sort)
    print(f"Comparisons for insertion sort: {comparisons}")
    print(f"Swaps for insertion sort: {swaps}")

current_time = time.time()
bubble_sort(my_list2)
print(f"Time for bubble sort: {time.time() - current_time}")

my_list2 = [5,3,4,1,2]
current_time = time.time()
selection_sort(my_list2)
print(f"Time for selection sort: {time.time() - current_time}")

my_list2 = [5,3,4,1,2]
current_time = time.time()
insertion_sort(my_list2)
print(f"Time for insertion sort: {time.time() - current_time}")