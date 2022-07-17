from re import I
from xml.sax.xmlreader import InputSource

# Buble Sort


def bubblesort(list):
    for x in range(len(list)-1, 0, -1):
        for y in range(x):
            if list[y] > list[y+1]:
                temp = list[y]
                list[y] = list[y+1]
                list[y+1] = temp

# Insertion Sort


def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i-1
        next_element = InputList[i]
    while (InputList[j] > next_element) and (j >= 0):
        InputList[j+1] = InputList[i]
        j -= 1
    InputList[j+1] = next_element

# Merge Sort


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    # find middle pointand devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))


def merge(left_half, right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

# Shell Sort


def shellSort(input_list):
    gap = len(input_list) // 2
    while gap > 0:
        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
# Sort the sub list for this gap
            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j -= gap
                input_list[j] = temp
        # Reduce the gap for the next element
        gap //= 2


def selection_sort(input_list):
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range(idx + 1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
# Swap the minimum value with the compared value
        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]


l = [19, 2, 31, 45, 30, 11, 121, 27]
selection_sort(l)
print(l)

list = [19, 2, 31, 45, 30, 11, 121, 27]
shellSort(list)
print(list)
