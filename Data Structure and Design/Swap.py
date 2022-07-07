#Code_1
def swapPositions1(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
 
# Driver function
List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
 
print(swapPositions1(List, pos1-1, pos2-1))
#Code_2
def swapPositions2(list, pos1, pos2):
     
    # popping both the elements from list
    first_ele = list.pop(pos1)  
    second_ele = list.pop(pos2-1)
    
    # inserting in each others positions
    list.insert(pos1, second_ele) 
    list.insert(pos2, first_ele) 
     
    return list
 
# Driver function
List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
 
print(swapPositions2(List, pos1-1, pos2-1))
#Code_3
def swapPositions3(list, pos1, pos2):
     
    # popping both the elements from list
    first_ele = list.pop(pos1)  
    second_ele = list.pop(pos2-1)
    
    # inserting in each others positions
    list.insert(pos1, second_ele) 
    list.insert(pos2, first_ele) 
     
    return list
 
# Driver function
List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
 
print(swapPositions3(List, pos1-1, pos2-1))

#Code_4
def swapPositions4(list, pos1, pos2):
 
    # Storing the two elements
    # as a pair in a tuple variable get
    get = list[pos1], list[pos2]
      
    # unpacking those elements
    list[pos2], list[pos1] = get
      
    return list
 
# Driver Code
List = [23, 65, 19, 90]
 
pos1, pos2  = 1, 3
print(swapPositions4(List, pos1-1, pos2-1))