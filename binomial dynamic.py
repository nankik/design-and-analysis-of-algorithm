n=int(input("Enter total number of ways : "))
r=int(input("Enter number to  be selected: "))
def bottom_up(n):
      bino=[0,1]
      for i in range(2,n+1):
            bino.append(bino[-1]*i)
      return bino

b=bottom_up(n)          
binomial=b[n]/(b[n-r]*b[r])
print(binomial)
