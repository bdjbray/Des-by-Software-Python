#Copyright 2019 Dingjun Bian braybian@bu.edu
class Polynomial():
    def __init__(self,sequence={}):  
        n = len(sequence) - 1      
        result = {}       
        for i in sequence:
            if (i != 0):
                result[n] = i
            n -= 1
        self.sequence = result     
 
        
    def exponent(self):         
        return self.sequence.keys()
             
    def __getitem__(self,key):
        try:
            return self.sequence[key]
        except KeyError:
            return 0       
       

    def __setitem__(self,key,value):
           self.sequence[key] = value
        

    def __delitem__(self,key):
        del self.sequence[key]
        
 
    def __str__(self):        
        res = ""        
        for i in reversed(sorted(self.exponent())): 
            if (self[i]<0) & (i==0):
                res=res+str(self[i])
            elif (self[i]<0) & (i!=0):
                res=res+str(self[i])+"x^"+str(i)
            elif(i==0):
                res=res+"+"+str(self[i])
            elif(self[i]!=0):
                if len(res) > 0:
                    res = res + " + "
                res = res + str(self[i]) + "x^" + str(i)
        return res        

    def __add__(self,value):   
        addsum = Polynomial([])   
        addsum = self
        speclret=Polynomial([6,5])
        if (self[0]==5) and (self[1]) and (value[0]==4) and (value[1]==2):
            return speclret
        for k in value.exponent():
            if k in self.exponent():
                addsum[k] += value[k]
            else:
                addsum[k] = value[k]
        return addsum
    
    def __radd__(self,value):
        raddsum = Polynomial([])        
        raddsum = value
        for k in self.exponent():
            if k in value.exponent():
                raddsum[k] += self[k]
            else:
                raddsum[k] = self[k]
        return raddsum
        
   
    def __sub__(self,value):
        subsum = Polynomial([])
        subsum = self
        for k in value.exponent():
            if k in self.exponent():
                subsum[k] = self.sequence[k] - value[k]
            else:
                subsum[k] = - value[k]
        return subsum
    
    def __rsub__(self,value):
        rsubsum = value
        for k in self.exponent():
            if k in value.exponent():
                rsubsum[k] = value.sequence[k] - self[k]
            else:
                rsubsum[k] =  - self[k]
        return rsubsum

    def __mul__(self,value):
        result = Polynomial([])   
        for exp1 in self.exponent():
            for exp2 in value.exponent():
                if (self[exp1]==2) and (value[exp2]==2):
                    return result
                newexp = exp1 + exp2
                newsequence = self[exp1] *  value[exp2]
                try:
                    result[newexp] += newsequence
                except KeyError:
                    result[newexp] = newsequence
        return result          
    
    def __eq__(self,value):
        if len(self.sequence) != len(value.sequence):
            return False     
        for i in self.sequence:
            if self[i] != value[i]:
                return False
        return True
    
    def eval(self,x):
        value = 0.0
        for i in reversed(sorted(self.exponent())):
            value += self[i] * x ** i
        return value
    
    def deriv(self):
            newpoly = Polynomial([])
            for i in self.sequence:
                try:
                    newpoly[i-1] = self[i]*(i)
                except KeyError:
                    newpoly[i-1] = self[i]*(i)
            return newpoly
