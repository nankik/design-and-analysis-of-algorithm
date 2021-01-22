def heap_sort(l):
      for i in range(len(l)-1,0,-1):      #total iterations
            for j in range(i,0,-1):             #max heap
                  if j%2==0:
                        parent=int(j/2)-1
                  else:
                        parent=int(j/2)
                  if l[parent]<l[j]:
                              l[j],l[parent]=l[parent],l[j]
            print ("max heap=",l[0:i+1])
            l[0],l[i]=l[i],l[0]
length=int(input("Enter number of elements: "))
l=[]
for i in range(length):
      l.append(int(input("Enter an element: ")))                 
heap_sort(l)     
print(l)                   
