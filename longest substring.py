a=input("Enter a string:  ")
b=""
for i in a:
      if i  not in b:
            b+=i
print("Longest substring from  '",a,"' without repeating any characters is '",b,"'")
print("Length=",len(b))
