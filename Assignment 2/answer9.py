# Write a binary search function. It should take a sorted sequence and the item it is looking for. It should return the
# index of the item if found. It should return -1 if the item is not found.
def binary_search(list, element):
    low = 0
    high = len(list) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if list[mid] < element:
            low = mid + 1
        elif list[mid] > element:
            high = mid - 1
        else:
            return mid
    return -1


list = [1, 2, 3, 5, 6, 8, 9, 11, 13, 23, 24]
element = 5
result = binary_search(list, element)
if result != -1:
    print("Element Present In Index", str(result))
else:
    print("Element Not Found In The list")
