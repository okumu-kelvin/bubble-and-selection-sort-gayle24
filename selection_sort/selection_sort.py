def selection_sort(arr):
    # TODO: Implement selection sort
    n = len(arr)
    # set outer loop to limit how many times the inner loop will run
    for i in range(n-1):
        # set the minimum value in the list to be the first index
        minim = i
        # inner loop checks all values in the list if they are smaller than the minimum value
        for j in range(i+1, n):
            # if current value is less than minimum value, it is set as the new minimum value
            if arr[j] < arr[minim]:
                minim = j
        # place the minimum value correctly before all other values
        arr[i], arr[minim] = arr[minim], arr[i]
    return arr

# test run
# print(selection_sort([2,8,4,3,1]))