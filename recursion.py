def bsearch(list, idx0, idxn, val):
    if idxn < idx0:
        return None
    else:
        midval = idx0 + ((idxn - idx0) // 2)
    if list[midval] > val:
        return bsearch(list, idx0, midval-1, val)
    elif list[midval] < val:
        return bsearch(list, midval+1, idxn, val)
    else:
        return midval


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 15, 16, 17]
print(bsearch(list1, 0, 15, 10))
print(bsearch(list1, 0, 15, 11))
