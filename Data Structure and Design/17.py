#Bucket_Sort
def isEmpty(S):
    return len(S)==0
def bucket_sort(S,N):
    B=[[]]*N
    print(B)

    while not isEmpty(S):
        f=S[0]
        S.pop(0)
        B[f[0]].append(f)
    for i in range(N):
        while not isEmpty(B[i]):
            f=B[i][0]
            B[i].pop(0)
            S.append(f)
    #S=sorted(S)
    return S

print(bucket_sort([(1,2,4),(2,5,3),(2,4,2),(5,4,1),(1,1,5)],10))

def radix_sort(S):
    N=int(input())
    S=sorted(bucket_sort(S,N))
    return S

#print(radix_sort([(1,2,4,4,4),(2,5,3,4,5),(2,4,2,9,8),(5,4,1,7,8),(1,1,5,5,7)]))


def binary_sort(S):
    S=sorted(bucket_sort(S,2))
    return S

print(binary_sort([(1,1,0,1),(0,0,0,1),(1,0,0,1),(0,0,1,0),(1,1,1,0)]))








