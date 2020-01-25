#Copyright 2019 Dingjun Bian braybian@bu.edu
Table = "{:<6} {:<22} {:<22} {:<22}"
print(Table.format('Bytes','Largest Unsigned Int','Minimum Signed Int','Maximum Signed Int'))
lu=[0]*10
maxs=[0]*10
mins=[0]*10

for c in range(1,9):
  for i in range(c*8):
      lu[c]=lu[c]+2**i
  for j in range(c*8-1):
      maxs[c]=maxs[c]+2**j
  mins[c]=(maxs[c]+1)*-1
  print(Table.format(c,lu[c],mins[c],maxs[c]))
    
