def insertion_sort(l):
      for i in range(1,len(l)):
            for j in range(i,0,-1):
                  if l[j]<l[j-1]:
                        l[j-1],l[j]=l[j],l[j-1]
            print (l)

def selection_sort(l):
      for i in range(len(l)):
            least=i
            for j in range(i,len(l)):
                  if l[least]>l[j]:
                        least=j
            l[i],l[least]=l[least],l[i]
            print(l)

def bubble_sort(l):
      for i in range(len(l),1,-1):
            for j in range(0,i-1):
                  if l[j]>l[j+1]:
                        l[j],l[j+1]=l[j+1],l[j]
            print(l)
import random

def quick_sort(l,lb,ub):
      pivot=random.randrange(lb,ub)
      i=lb
      j=ub
      while j>i :
            while l[i]<=l[pivot] and i!=ub:
                 i+=1
            while l[j]>=l[pivot] and j!=lb:
                  j-=1
            if j>i:
                  l[i],l[j]=l[j],l[i]
      else:
            if pivot<j:
                  l[j],l[pivot]=l[pivot],l[j]
            elif pivot>i:
                  l[i],l[pivot]=l[pivot],l[i]
      print (l)
      if j-lb>=2:
            quick_sort(l,lb,j-1)
      if (ub-j)>=3:
            quick_sort(l,j+1,ub)
      
      
length=int(input("Enter number of elements: "))
l=[]
for i in range(length):
      l.append(int(input("Enter an element: ")))
#insertion_sort(l)
#selection_sort(l)
#bubble_sort(l)
quick_sort(l,0,length-1)
