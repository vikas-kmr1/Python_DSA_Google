
def binary_Search(l,key,start,end):
    if(start==end):
        if l[start]==key:
            return start
        else:
            return -1
    else:
        mid=int((start+end)/2)

        if(l[mid]==key):
            return mid
        elif(key<l[mid]):
            return (binary_Search(l,key,start,mid-1))
        elif(key>l[mid]):
            return (binary_Search(l,key,mid+1,end))


print("Enter a list of numbers")
l= list(map(int, input().split()))
l.sort()
print(l)

key=int(input("Enter a Element to be search:"))
index=binary_Search(l,key, start=0, end=len(l))
if(index==-1):
    print(f"{key} not found")
if(index !=-1):
    print(f"{key} found at pos {index+1}")



