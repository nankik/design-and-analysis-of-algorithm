v=int(input("Enter number of vertices: "))
e=int(input("Enter number of edges: "))
from math import inf
l=[(0,0)]                          #for  index,(vertex,distance)
edge=[]                 #(start,stop,distance)
print("Consider start vertex 0  and rest vertices numbered upto ", v-1)
for i in range(1,v):
      l.append((0,inf))       #distance initiated
for i  in range(e):
      start=int(input("Enter edge 1:  "))
      stop=int(input("Enter edge  2: "))
      distance=int(input("Enter distance between the two edges:  "))
      edge.append((start,stop,distance))
for  i  in edge:
      if l[i[0]][1]!=inf:              #can be checked
            if l[i[1]][1]>(i[2]+l[i[0]][1]):
                  l[i[1]]=(i[0],i[2])
      else:
            edge.append(i)        #cannot be checked now
      if l[i[1]][1]!=inf:              #can be checked
            if l[i[0]][1]>(i[2]+l[i[1]][1]):
                  l[i[0]]=(i[1],i[2])
      else:
            edge.append(i)        #cannot be checked now
print  (l)
      
