from random import randrange

def swap(a,i,j):
     s=a[i]; a[i]=a[j]; a[j]=s
     return a

def partition(a,left,right,pivot): 
   swap(a,left,pivot)
   l=left; r=right     
   while l<r: 
        while a[r]>=a[left] and l<r:
              r=r-1
        while a[l]<=a[left] and l<r:
              l=l+1
        swap(a,l,r)     
   swap(a,left,l)
   for i in range(l+1):
      if a[-1]<=a[i]:
         a.insert(i,a[-1])
         a.pop()
   return a,l



def quicksort(a,l,r):
   if l<r: 
      p=randrange(l, r) 
      a,j=partition(a,l,r,p)
      quicksort(a,l,j-1)
      quicksort(a,j+1,r)
   return a


a=[randrange(100) for i in range(12)]
print(a)

#print(quicksort(a,0,len(a)-1))
print(partition(a,0,len(a)-1,len(a)//2-3))
print(len(a)//2-3)
print(quicksort(a,0,len(a)-1))


def merge(a,b):
    i=0; j=0; c=[]
    while i<len(a) and j<len(b): 
        if a[i]<=b[j]: 
            c.append(a[i])
            i=i+1
        else: 
            c.append(b[j])
            j=j+1 
    while i<len(a):
        c.append(a[i]); i=i+1 
    while j<len(b): 
        c.append(b[j]); j=j+1
    return c    

def mergesort(a):
    if len(a)>1: 
       m=int(len(a)/2)
       return merge(mergesort(a[0:m]),mergesort(a[m:len(a)]))
    else: 
       return a
print("Merge list")
print(mergesort([4,2,1,5,6,10,-5,-4,100]))