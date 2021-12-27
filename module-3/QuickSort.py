def partition(array, low, high):

  # choose the last element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # compare each element with pivot
  for j in range(low, high):
    if array[j] < pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    pi = partition(array, low, high)

    quickSort(array, low, pi - 1)

    quickSort(array, pi + 1, high)



if __name__=="__main__":
    array = [10, -7, -8, 9, 1, 5,8,10,80]
    print(f'UnSorted array: {array}')
    quickSort(array,0, len(array) - 1)

    print(f'Sorted array: {array}')

