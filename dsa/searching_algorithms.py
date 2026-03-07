# linear search

fruits = ["apple","orange","banana"]
numbers = [75,223,8,943,22,4,56,7,3,22,56]
sorted_list = [1,2,3,4,5,6,7,8,9,10]

def linear_search(list_to_search,item_to_find):
    list_to_search = sorted(list_to_search)
    for item in list_to_search:
        if item == item_to_find:
            return "Item found"
        if item > item_to_find:
            break
    return "Item not found"

def binary_search(sorted_list,item_to_find):
    low = 0
    high = len(sorted_list)-1
    mid = (low+high)//2

    while low < high:
        mid = (low+high)//2
        if item_to_find < mid:
            high = mid-1
        if item_to_find > mid:
            low = mid+1
        if item_to_find == mid:
            return "Item found"
    return "Item not found"

print(binary_search(sorted_list,11))
