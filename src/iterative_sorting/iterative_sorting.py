# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        if smallest_index:
            arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Make a flag to show if swaps have occurred
    swaps_occurred = True
    # Run until you get through a loop without any swaps
    while swaps_occurred:
        swaps_occurred = False
        # For each element in the array...
        for i in range(len(arr) - 1):
            # Check it's neighbor to the right...
            if arr[i] > arr[i+1]:
                # If neighbor is smaller, swap and make Flag true
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps_occurred = True
    return arr


# STRETCH: implement the Count Sort function below

def count_sort(arr, maximum=-1):

    return arr
