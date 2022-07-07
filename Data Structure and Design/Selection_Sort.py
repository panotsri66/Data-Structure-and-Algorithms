import numpy as np
def Selection_Sort(A):
    
    for i in range(len(A)-1):#---> Do (N-1) iterations#
                                                      #
        index=i                                       #
                                                      #
        for j in range(i,len(A)): #-------------------#
                                                      #
            if A[index]>A[j]:                         #
                index=j                               #-------> O(N^2)
                                                      #
        if index != i:                                #
                                                      #
            A[index],A[i]=A[i],A[index]#--------------#
        

    return A


#print(Selection_Sort([i for i in "index"]))