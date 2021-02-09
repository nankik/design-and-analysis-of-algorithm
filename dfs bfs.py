d={}
v=int(input("Enter number of vertices: "))
for i in range(1,v+1):
      new_vertex=input("Enter value of vertex "+str(i)+" : ")
      connect=input("Enter connecting node values with spaces: ").split(" ")
      d[new_vertex]=connect

def bfs(node):
      queue=[]
      visited=[]
      visited.append(node)
      queue.append(node)
      while queue:
            s=queue.pop(0)
            print(s,  end="\t")
            for i  in d:
                  if i not in visited:
                        visited.append(i)
                        queue.append(i)
#start=input("Enter start node:")
#if start  in  d:
      #bfs(start)

visited=[]
def  dfs(node):
      if node not in visited:
            print (node,  end="\t")
            visited.append(node)
            if d[node]!=[""]:
                  for i in d[node]:
                        dfs(i)
start=input("Enter start node:")
if start  in  d:
      dfs(start)
