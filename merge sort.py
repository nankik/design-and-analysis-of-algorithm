length=int(input("Enter number of elements: "))
l=[]
for i in range(length):
      l.append(int(input("Enter an element ")))
      
def mergesort(arr):
    if len(arr) > 1:
        mid =int( len(arr)/2)
        L = arr[0:mid]
        R = arr[mid:length]
        mergesort(L)
        mergesort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


mergesort(l)
print("Sorted array is: ",)
for i in l:
      print (i,)
