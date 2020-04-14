# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    elements = len(arrA) + len(arrB)
    merged_arr = [] * elements
# TO-DO
    a, b = 0, 0
# starting at beginning of `a` and `b`
# compare the next value of each
# add smallest to `merged_arr`
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1
    if a == len(arrA):
        merged_arr.extend(arrB[b:])
    else:
        merged_arr.extend(arrA[a:])

    return merged_arr


'''
# 1. While your data set contains more than one item, split it in half
# 2. Once you have gotten down to a single element, you have also *sorted* that element
    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled
'''


'''
RULES FOR RECURSION
1. Must have a base case.
2. Must change state toward the base case.
3. Must call itself, recursively.
'''

# TO-DO: implement the Merge Sort function below USING RECURSION


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
