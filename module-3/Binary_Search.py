"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_Search(input_array, value,start,end): # = [1, 3, 9, 11, 15, 19, 29]
    #"""Your code goes here."""
    while start<=end:
        mid=int((start+end)/2)

        if input_array[mid]==value:
            return mid
        elif input_array[mid]<value:
            start=mid+1
        elif input_array[mid]>value:
            end=mid-1
    return -1

test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_Search(test_list, test_val1,0,len(test_list)-1))
print(binary_Search(test_list, test_val2,0,len(test_list)-1))