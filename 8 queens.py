positions=[]
def queens(pos,positions,q):
      if 0 not in pos and pos not in positions:
            positions.append(pos)
      elif 0 not in pos:
            pass
      else:
            for i  in range(8):
                  rd=i+q
                  ld=q-i
                  if  pos[i]==0  and  rd not in rdaig and q not in pos and ld  not  in ldaig:
                        rdaig.append(rd)
                        ldaig.append(ld)
                        pos[i]=q
                        queens(pos,positions,q+1)              
for i  in range(8):     #initiation
      pos=[0,0,0,0,0,0,0,0]
      rdaig=[1+i]    #right daignol
      ldaig=[i-1]    #left  daignol
      pos[i]=1
      queens(pos,positions,2)
#To print
for i in positions:
      print("="*60)
      for j in i:
            for k in range(8):
                  if j==k+1:
                        print("Q",end="\t")
                  else:
                        print("@",end="\t")
            print()
