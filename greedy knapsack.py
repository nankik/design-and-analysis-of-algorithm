n=int(input("Enter number of elements:"))
l=[]        #stores input as (profit,weight)
l1=[]       #stores profit/weight
output=[]
for i in range(n):
      p=float(input(("Enter profit recieved by "+str(i+1)+"  object: ")))
      w=float(input(("Enter weight of "+str(i+1)+" object: ")))
      l.append((p,w))
      x=round(p/w,2)
      l1.append(x)
      output.append(0)
weight=int(input("Enter allowed weight:"))
w=0
p=0
for i in range(n):
            m=i
            for j in range(n):      #finding max weight
                  if l1[m]<l1[j]:
                        m=j
            if l[m][1]+w<=weight:          # comparing weight
                  p+=l[m][0]
                  w+=l[m][1]
                  output[m]=1
                  l1[m]=0
            else:
                  l1[m]=0
                  #for fractional
                  #if  weight-w>0:
                        #output[m]=round(l[m][1]/(weight-w),2)
                        #p+=l[m][0]*output[m]
                        #w+=weight-w
                  break
print (output)
print("Total weight=",w)
print("Total profit=",p)
