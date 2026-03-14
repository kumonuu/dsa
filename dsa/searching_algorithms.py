import time

fruits = ["apple","orange","banana"]
numbers = [75,223,8,943,22,4,56,7,3,22,56]
sorted_list = [1,2,3,4,5,6,7,8,9,10]
large_list = []


for i in range(1,100001):
    large_list.append(i)

def linear_search(list_to_search,item_to_find):
    list_to_search = sorted(list_to_search)
    for item in list_to_search:
        if item == item_to_find:
            return "Item found"
        if item > item_to_find:
            break
    return "Item not found"

def linear_search_mississippi(list_to_search,item_to_find):
    list_to_search = sorted(list_to_search)
    letter_count = 0
    for item in list_to_search:
        if item == item_to_find:
            letter_count += 1
        if item > item_to_find:
            break
    return letter_count

def binary_search(sorted_list,item_to_find):
    low = 0
    high = len(sorted_list)-1
    mid = (low+high)//2

    while low < high:
        mid = (low+high)//2
        if item_to_find < sorted_list[mid]:
            high = mid-1
        if item_to_find > sorted_list[mid]:
            low = mid+1
        if item_to_find == sorted_list[mid]:
            return "Item found"
    return "Item not found"

start_time = time.time()
print(linear_search(large_list,99999))
print(time.time() - start_time)

start_time = time.time()
print(binary_search(large_list,99999))
print(time.time() - start_time)

print(linear_search_mississippi("MISSISSIPPI",'S'))
print(linear_search_mississippi("MISSISSIPPI",'P'))