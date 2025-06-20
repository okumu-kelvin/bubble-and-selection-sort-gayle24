def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort

    #set the length of the input list
    n = len(unsorted_list);

    # iterate through the list n-1 times for each value
    for i in range(n-1):
        for j in range(n-i-1): #for each time the list is sorted, the next iteration will omit the largest value at the end
            # for two adjacent values, they are swapped if first value is larger than the second
            if unsorted_list[j] > unsorted_list[j+1]: 
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    return unsorted_list

