length=int(input("Enter number of elements: "))
l=[]
for i in range(length):
      l.append(int(input("Enter  an element in sorted order: ")))
key=int(input("Enter the element to be searched: "))
def iterative(l,key):
      lb=0
      found=0
      ub=length-1
      while lb<ub:  
            mid=int((lb+ub)/2)
            print("mid found")
            if l[mid]==key:
                  print ("Element found at index",mid+1)
                  found=1
                  break
            elif l[mid]<key:
                  lb=mid+1
            elif l[mid]>key:
                  ub=mid-1
      if found==0:
            print("Element  not found")
def recursive_binary(l,key,lb,ub):
      mid=int((lb+ub)/2)
      print("mid found")
      if lb>ub:
            print("Element  not found")
      elif l[mid]==key:
            print ("Element found at index",mid+1)
      elif key>l[mid]:
            lb=mid+1
            recursive_binary(l,key,lb,ub)
      elif key<l[mid]:
            ub=mid-1
            recursive_binary(l,key,lb,ub)
recursive_binary(l,key,0,length-1)
