
def selection_sort(alist):
    for index, x in enumerate(alist):
        min_index = index
        for index2, x2 in enumerate(alist[index:]):
            if alist[index2+index] < alist[min_index]:
                min_index = index2+index
        alist[index], alist[min_index] = alist[min_index], alist[index]
