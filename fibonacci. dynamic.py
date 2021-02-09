n=int(input("Enter number of elements for fibonacci series: "))
def top_down(n):
      if n == 0:
            return 0
      if n == 1:
            return 1
      return top_down(n-1) + top_down(n-2)

print(top_down(n))

def bottom_up(n):
      f=[0,1]
      for i in range(2,n+1):
            f.append(f[-1]+f[-2])
      print (f[n])
            
bottom_up(n)
            
