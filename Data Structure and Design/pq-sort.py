def pq_sort(C):
    n=len(C)
    P=PriorityQueue()
    for i in range(n):
        element=C.delete(C.first())
        P.add(element,element)
    for i in range(n):
        (k,v)=P.remove_min()
        C.add_last(v)
