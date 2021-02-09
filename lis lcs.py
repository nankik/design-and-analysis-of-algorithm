print("Longest  common subsequence")
a=input("Enter string1: ")
b=input("Enter string2: ")
print("Longest subsequence from  '",a,"' and '",b,"'", end="is : ")
def lcs(a,b):
      bx=b
      lcs=""
      for i in a:
            for j in range(len(bx)):
                  if i.lower()==bx[j].lower():
                        lcs+=i
                        bx=bx[j+1:]
                        break
      return lcs
l1=lcs(a,b)
l2=lcs(b,a)
if len(l1)>len(l2):
      l=l1.upper()
elif len(l1)<len(l2):
      l=l2.upper()
elif l1.upper()==l2.upper():
      l=l1.upper()
else:
      l=[l1,l2]
print(l)
if type(lcs)==str:
      print("Length=",max(len(l1),len(l2)))

"""print("Longest increasing subsequence")        
n=int(input("Enter length of sequence: "))
l=[]
for i in range(n):
      l.append(int(input("Enter sequence element:")))

      lis=1
if n==0:
      lis=0
i=0
while True:
      k=0
      for  j in range(i+1,len(l)):
            if l[j]>=l[i]:
                  i=j
                  lis+=1
                  k=1
                  break
      if k==0:
            break
print(lis)"""
                  
                  
