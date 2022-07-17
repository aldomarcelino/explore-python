arr1 = [3, 2, 4]
target1 = 6


def two_sum(arr, target):
    values = {}
    for i, elem in enumerate(arr):
        comp = target - elem
        if comp in values:
            return[values[comp], i]
        values[elem] = i
    return []


list1 = two_sum(arr1, target1)
print(list1)
