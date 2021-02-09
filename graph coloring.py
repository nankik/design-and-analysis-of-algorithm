class graph_node:
      def __init__(self,name,*neighbour):
            self.name=name.strip(" ")
            self.neighbour=neighbour
            self.color="red"
class graph:
      def __init__(self):
            n=int(input("Enter number of nodes: "))
            self.nodes=[]
            i=0
            while i<n:
                  name=input("Enter name of "+str(i+1)+" node:  ")
                  neighbour=input("Enter name of neighbours using spaces: ").split()
                  g=graph_node(name,neighbour)
                  self.nodes.append(g)
                  i+=1
                  print(len(self.nodes)," nodes created")
      def find(self,name):
            for  i  in self.nodes:
                  if i.name==name:
                        return i
      def colour(self):
            colors=["red","blue","green","yellow","orange","violet","black","white"]
            color_used=set()
            for i in self.nodes:
                  color_used.add(i.color)
                  for j in i.neighbour:
                        for k in j:
                              neigh=self.find(k)
                              if i.color==neigh.color:
                                    neigh.color=colors[colors.index(i.color)+1]
            for i in self.nodes:
                  print("Colour of ",i.name," = ",i.color)
            print("Total number of colours used = ",len(color_used))
                  
g1=graph()
g1.colour()

                  
            
