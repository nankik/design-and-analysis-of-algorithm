v=int(input("Enter number of vertices: "))
e=int(input("Enter number of edges: "))
from math import inf
l=[(0,0)]                       #for  index,(vertex,distance)
edge=[]                       #(distance,start,stop)
print("Consider start vertex 0  and rest vertices numbered upto ", v-1)
for i in range(1,v):
      l.append((0,inf))       #distance initiated
for i  in range(e):
      start=int(input("Enter edge 1:  "))
      stop=int(input("Enter edge  2: "))
      distance=int(input("Enter distance between the two edges:  "))
      edge.append((distance,start,stop))
edge.sort()
for i in  edge:
      if  l[i[1]]==(0,inf):
            l[i[1]]=(i[2],i[1])
      if l[i[2]]==(0,inf):
            l[i[2]]=(i[1],i[0])
print(l)
              
