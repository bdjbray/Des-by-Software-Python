#Copyright 2019 Dingjun Bian braybian@bu.edu
import numpy as np

a=input()  #read input generate and delete the space
b=input()
a=a.replace("(","")
a=a.replace(")","")
a=a.replace("[","")
a=a.replace("]","")
b=b.replace("(","")
b=b.replace(")","")
b=b.replace("[","")
b=b.replace("]","")
a = a.split(' ')
b = b.split(' ')
a1=len(a)
b1=len(b)



A=np.zeros(a1)   #acquire the array from the modified input
for i in range(a1):
    A[i]=a[i]
B=np.zeros(b1)
for i in range(b1):
    B[i]=b[i]
new1=np.convolve(A, B)
new2=str(new1)
new2=new2.replace("]","")
new2=new2.replace("[","")
print(new2)
