from  random import randrange
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
   return a,l

def quicksort(a,l,r):
   if l<r: 
      i=randrange(l, r)  # choice of a pivot point
      a,j=partition(a,l,r,i)
      quicksort(a,l,j-1)
      quicksort(a,j+1,r)
   return a

a=[6,5,4,5,6,-4,4,1,1,0,-9,7,8,8,4,2,1,3]

#print(quicksort(a,0,len(a)-1))

def generatic_merge(A,B):
    S=[]
    while len(A)>0 and len(B)>0:
        a=A[0]
        b=B[0]
        if a < b:
            S.insert(0,a)
            A.pop(0)
        elif b<a:
            S.append(b)
            B.pop(0)
        else:
            S.append(a)
            A.pop(0)
            B.pop(0)
    while len(A)>0:
        S.insert(0,A[0])
        A.pop(0)
    while len(B)>0:
        S.append(B[0])
        B.pop(0)    
    return S

print(generatic_merge([1,4,5,6,7,9],[-1,1,5,-10,7,8]))