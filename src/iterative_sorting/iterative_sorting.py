# TO-DO: Complete the selection_sort() function below 
# Starting
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        for l in range(i+1, len(arr)):
            if arr[smallest_index] > arr[l]:
                smallest_index = l     



        # TO-DO: swap
        s = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = s



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    

    
    for i in range(len(arr)-1,0,-1): # length of array -1, range of 0, reverse order -1
        for l in range(i):
            if arr[l] > arr[l+1]:
                swap = arr[l]
                arr[l] = arr[l+1]
                arr[l+1] = swap
                    
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr