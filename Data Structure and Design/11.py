from Selection_Sort import Selection_Sort

class Node:
    def __init__(self,k,v):
        
        self.key=k
        self.value=v
        self.next=None  
class PriorityQueue:
    class Node:
        def __init__(self,k,v):
        
            self.key=k
            self.value=v
            self.next=None
            
    
    def __init__(self):
        
        self.front = None
        self.size=0
    
    def isEmpty(self):
        if self.front == None:
            return (True)
        else:
            return (False)

    def insert(self,key,value):

        if self.isEmpty() == True:

            self.front=Node(key,value)
        
            self.size+=1


        else:

            if self.front.key > key: #

                new=Node(key,value)
                
                new.next=self.front

                self.front=new

                self.size+=1
        
            else:

                A=Node(key,value) 

                currentnode=self.front

                while currentnode.next:
                    
                    if key < currentnode.next.key:
                        break

                    currentnode=currentnode.next

                
                A.next=currentnode.next
                currentnode.next=A

                self.size+=1


    def remove_min(self):
        
        if self.isEmpty():
            return

        else:
            A=self.front.value
            self.front=self.front.next
            self.size-=1
            return A
            

    def traverse_node(self):

        if self.isEmpty():
            return
        else:
            cur=self.front
            while  cur is not None:
                print (cur.value)
                cur=cur.next

    def Pri_size(self):
        return self.size

    def min_key(self):
        if self.isEmpty():
            return
        else:
            return(self.front.key)
    def min_element(self):
        if self.isEmpty():
            return
        else:
            return(self.front.value)

    '''def min_element(self):
        if self.isEmpty():
            return
        else:    
            Array=[]
            cur=self.front
            while cur is not None:
                Array.append(cur.value)
                cur=cur.next
            S=Selection_Sort(Array)
            return(S[0])'''
    
    def Sort_element(self):
        if self.isEmpty():
            return
        else:    
            Array=[]
            cur=self.front
            while cur is not None:
                Array.append(cur.value)
                cur=cur.next
            Array=Selection_Sort(Array)   
            return Array

    def minimum(self):
        if self.isEmpty():
            return
        else:
            A=self.front
            min=A.value
            while A.next:
                if min <= A.next.value:
                    A=A.next
                    
                elif min > A.next.value:
                    min=A.next.value
                    A=A.next
            return min
                    
                

    

A=PriorityQueue()
A.insert(1,100)
A.insert(2,-50)
A.insert(3,89)
A.insert(4,-2)
A.insert(5,6)
A.insert(6,-9)
A.insert(7,10)
A.insert(8,66)
print("\nSorting element")
print(A.Sort_element())
print("\nremoving minimum element with minimum key")
print(A.remove_min())
print("\ntraverse nodes")
print(A.traverse_node())
print("\nmininmum")
print("\nเรียกใช้ min_key()")
print(A.min_key())
print("\nเรียกใช้ min_element()")
print(A.min_element())