# First Option, USING XOR (Binary)

def find_unique_element(arr):
    unique_element = 0
    for num in arr:
        unique_element ^= num
    return unique_element

arr1 = [1, 1, 10, 10, 9, 9, 5, 5, 6, 8, 8]
arr2 = [1, 3, 3]
arr3 = [9, 9, 4]

print(find_unique_element(arr1))
print(find_unique_element(arr2))
print(find_unique_element(arr3))

# =============================================================

# 2nd Option, USING SET:

def find_unique_element(arr):
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for num, cnt in count.items():
        if cnt == 1:
            return num

arr1 = [1, 1, 10, 10, 9, 9, 5, 5, 6, 8, 8]
arr2 = [1, 3, 3]
arr3 = [9, 9, 4]

print("*****************")
print(find_unique_element(arr1))
print(find_unique_element(arr2))
print(find_unique_element(arr3))
