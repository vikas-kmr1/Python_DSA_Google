def mergeSort(arr): # initial arr=[12, 11, 13, 5, 6, 7,1]
	if len(arr)>1:
		mid=len(arr)//2 # returns Quotient or floor division value
		Lt=arr[:mid]
		Rt=arr[mid:]

		# Sort the two halves
		mergeSort(Lt)
		mergeSort(Rt)

		i=0  #iterates over Lt
		j=0  # iterates over Rt
		k=0  # iterates over  array with  sorted element at correct position

		while i<len(Lt) and j<len(Rt):
			if Lt[i] <Rt[j]:
				arr[k]=Lt[i]
				i += 1
			else:
				arr[k]=Rt[j]
				j += 1
			k += 1

		# When we run out of elements in either Lt or Rt,
		# pick up the remaining elements and put in arr

		while i < len(Lt):
			arr[k] = Lt[i]
			i += 1
			k += 1

		while j < len(Rt):
			arr[k] = Rt[j]
			j+=1
			k += 1

# Driver Code
if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7,1]
	print("Given array is", end="\n")
	print(arr)
	mergeSort(arr)
	print("Sorted array is: ", end="\n")
	print(arr)


