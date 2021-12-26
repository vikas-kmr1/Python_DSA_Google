def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp




arr = [64, 34, 25, 12, 22, 11, 90]

print(arr)
bubbleSort(arr)
print ("Sorted array is:")
print(arr)