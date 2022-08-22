"""
repeat(numOfElements - 1) times
    set the first unsorted element as the minimum
    for each of the unsorted elements
        if element < currentMinimum
            set element as new minimum
    swap minimum with first unsorted position
    
    ----------------------------------------------------------------------------
[3, 44, 38, 5, 47, 15, 36, 26]
    so three is first minimum
    is 3 < 44 if it is move on to the next one until get to 26 (the last element in list) 
    then swap if necessary
    ----------------------------------------------------------------------------

    
    
    """

 
#TODO: not finished still need to implement

def selectionSort(list):
    curr_min = 0
  
  
    for i in range(len(list)):
        if list[i] < list[curr_min]:
            curr_min = list[i]
            # if it is 
            print('i: ', list[i] , 'IS < curr min: ', list[curr_min])
        else:
            print('i: ', list[i] , 'is not < curr min: ', list[curr_min])
    print(list)
        

#1 set the first element as the minimum, in this case 3



selectionSort([3, 1 , 44, 38, 5, 47, 15, 36, 26])