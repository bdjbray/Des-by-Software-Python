#copyright 2019 Dingjun Bian braybian@bu.edu
def is_happy(x):
 n=x
 num=str(n)
 sum =0
 for i in range(10):
    for j in num:
        sum+=int(j)**2
    if sum==1:
        return True
    else:
        num=sum
        sum=0
        num=str(num)
        

 return False     
 




def product_of_positives(seq):
  sum=1
  for i in seq:
   i=str(i)
   if i.count('.')==1:
      i=float(i)
      if i>0:
         sum=sum*i
         continue
   elif (i.isdigit()):
      i=int(i)
      if i>0  :
        sum=sum*i   

  return sum



def proper_divisors(n):
  if n==0:
      return (0)
  tur=[1]
  for i in range(2,n):
      if n%i==0:    
          tur.append(i)
  tur=tuple(tur)
  return tur


if __name__ == '__main__':
	# your test code here.
	pass
