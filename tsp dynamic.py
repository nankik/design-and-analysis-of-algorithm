v=int(input("Enter number of vertices: "))
print("Consider start vertex 1 upto ",v,"vertices")
v1={0}
l=[]
for i in range(v):
      d=[]
      v1.add(i)
      for j in range(v):
            if i==j:
                  d.append(0)
            else:
                  d.append(int(input("Enter distance of path from "+str(i+1)+" to "+str(j+1)+" : ")))
      l.append(d)
from itertools import permutations
p=list(permutations(v1-{0},v-1))
distance=[]
for i in p:
      d=l[0][i[0]]+l[i[-1]][0]     #distance from start
      for j in range(len(i)-1):
            d+=l[i[j]][i[j+1]]
      distance.append(d)
min_path=p[distance.index(min(distance))]
path=[1]
for i in min_path:
      path.append(i+1)
path.append(1)
print("Minimum distance=  ", min(distance))
print("Path=  ",path)
