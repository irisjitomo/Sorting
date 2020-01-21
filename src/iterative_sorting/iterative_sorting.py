# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i):
            smallest_index = smallest_index - j
            print('smallest', smallest_index)

        # TO-DO: swap




    return arr
selection_sort([1,2,3,4])


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for j in range(0, len(arr)):
        for i in range(j):
            left = i
            right = i + 1
            LHS = arr[left]
            RHS = arr[right]
            if RHS > LHS:
                LHS, RHS = RHS, LHS
    
        
    return arr

bubble_sort([1,2,3,4,5,6])


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr