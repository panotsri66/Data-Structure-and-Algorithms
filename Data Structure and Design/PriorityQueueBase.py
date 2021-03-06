from PositionalList import PositionalList
class Empty(Exception):
  pass
class PriorityQueueBase:
    class _Item:
        __slots__='_key','_value'
    
        def __init__(self,k,v):
            self._key = k
            self._value = v
        def __It__(self,other):
            return self._key < other._key
    
    def is_empty(self):
        return len(self)==0

class UnsortedPriorityQueue(PriorityQueueBase):
    def _find_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        small=self._data.first()
        walk=self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small=walk
            walk=self._data.after(walk)
        return small
    def __init__(self):
        self._data=PositionalList()
    def __len__(self):
        return len(self._data)
    def add(self,key,value):
        self._data.add_last(self._Item(key,value))
    def min(self):
        p=self._find_min()
        item=p.element()
        return (item._key,item._value)
    def remove_min(self):
        p=self._find_min()
        item=self._data.delete(p)
        return (item._key,item._value)

class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data=PositionalList()
    def __len__(self):
        return len(self._data)
    def add(self,key,value):
        newest=self._Item(key,value)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk,newest)
    def min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        p=self._data.first()
        item=p.element()
        return(item._key,item._value)
    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item=self._data.delete(self._data.first())
        return(item._key,item._value)