#Copyright 2019 Dingjun Bian braybian@bu.edu
def largest_double():
  ex1=2047-1024
  num1=1
  for i in range(1,53):
    num1=num1+(1/2)**i
  ld=num1*2**ex1
  return ld


def smallest_double():
  ex3=0
  num3=0
  i=1074
  num3=num3+(1/2)**i
  sd=num3*2**ex3
  return sd 
 
  
def largest_single():
  ex=255-128
  num=1
  for i in range(1,24):
    num=num+(1/2)**i
  ls=num*2**ex
  return ls


def smallest_single():
  ex2=0
  num2=0
  i=149
  num2=num2+(1/2)**i
  ss=num2*2**ex2
  return ss
 

def main():
  print(largest_double())
  print(smallest_double())
  print(largest_single())
  print(smallest_single())

if __name__ == '__main__':
  main()
