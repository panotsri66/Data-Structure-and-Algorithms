#1. Write a program to find the prefix average based on the pseudocode as shown in the class example with the time complexity of O(n^2) and O(n), respectively.
from timeit import timeit
from random import *
class Algorithm_Testing:
    def __init__(self):

            














# Prefix average in linear
     def prefixAverages2(X, n):
        A = []
        s = 0
        for i in range(n):
            s = s + X[i]
            S = s / (i+1)
            A.append(S)
        return A
    #print(prefixAverages2([1, 2, 3, 4,5,6], 6))

    #Prefix average in quadratic
    def prefixAverages1(X,n):
        A=[]
        for i in range(n):
            s=X[0]
            for j in range(1,i+1):
                s=s+X[j]
            S=s/(i+1)
            A.append(S)
        return(A)
#print(prefixAverages1([1, 2, 3, 4,5,6], 6))
'''for i in range(1,2):
    print(i)'''
#Random array
    def random_array():
        A=[]
        a=True
        while a:
            x=randint(-1000,1000)
            A.append(x)
            if len(A)==1000:
                a=False
        return A

#Generate array




#Testing
    '''time = timeit('prefixAverages2([1, 2, 3, 4,5,6,7], 7)', number=10, globals=globals())
    print(time)'''



from timeit import timeit
from random import *
class Array_Generator:
    data=10
    def __init__(self):
        self.list=[]
        self.random_array()
        self.num=None
    # Prefix average in linear
    def plus(self):
        Array_Generator.data+=1
        return Array_Generator.data
    def upgraded_array(self):
        self.plus()
        self.random_array()
    def random_array(self) -> object:
        a=True
        while a:
            x=randint(-1000,1000)
            self.list.append(x)
            if len(self.list)==Array_Generator.data:
                a=False

    def clear_list(self):
        self.list=[]


y=[]
x=[]
#Prefix average in quadratic
def prefixAverages1(X,n):
    A=[]
    for i in range(n):
        s=X[0]
        for j in range(1,i+1):
            s=s+X[j]
        S=s/(i+1)
        A.append(S)
    return(A)
def prefixAverages2(X, n):
    A = []
    s = 0
    for i in range(n):
        s = s + X[i]
        S = s / (i + 1)
        A.append(S)
    return A
Array=Array_Generator()
#เอาไว้test
def all():
    for j in range(1,100000):
        Array.upgraded_array()

        for i in range(49):
            total_time=0
            time = timeit('prefixAverages2(Array.list, len(Array.list))', number=10, globals=globals())
            total_time+=time
        T=total_time/50
        T=T*10000000
        '''print(T)
        print(Array.list)
        print(prefixAverages2(Array.list, len(Array.list)))'''
        y.append(T)
all()
#print(DATA)
'''print(y)'''
