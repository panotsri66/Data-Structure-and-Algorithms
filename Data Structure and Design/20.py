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
def swap(a,i,j):
     s=a[i]; a[i]=a[j]; a[j]=s
     return a

print(partition([1,5,9,4,3,2],0,5,3))