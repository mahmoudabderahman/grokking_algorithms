def binary_search(list, item):
    # low and high keep track of which part of the list you will search in.
    low = 0
    high = len(list)-1
    
    while low <= high: # while you have not narrowed it down to one element ....
        mid = int((low + high) / 2) # check the middle element
        guess = list[mid]

        if guess == item: # item is found
            return mid
        if guess > item: # if the guess was too high
            high = mid - 1
        else:
            low = mid + 1 # if the guess was too low
    return None

my_list = [1,3,5,7,9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))