
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # this operation inserts items at the end of the linked list
    # so we have to manipulate the tail node in O(1) running time
    def insert(self, data):

        new_node = Node(data)

        # when the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # there is at least 1 item in the data structure
        # we keep inserting items at the end of the linked list
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # we can traverse a doubly linked list in both directions
    def traverse_forward(self):

        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next

    def traverse_backward(self):

        actual_node = self.tail

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.previous

    def remove_node(self,data):
        # list is empty
        if self.head is None:
            return

        actual_node = self.head
        # we have to track the previous node for future pointer updates
        # this is why doubly linked lists are better - we can get the previous
        # node (here with linked lists it is impossible)
        previous_node = None

        # search for the item we want to remove (data)
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next

        # search miss
        if actual_node is None:
            return

        # the head node is the one we want to remove
        if previous_node is None:
            self.head = actual_node.next
        else:
            # remove an internal node by updating the pointers
            # NO NEED TO del THE NODE BECAUSE THE GARBAGE COLLECTOR WILL DO THAT
            previous_node.next = actual_node.next
            actual_node.next.previous=actual_node.previous



if __name__ == '__main__':

    linked_list = DoublyLinkedList()
    linked_list.insert(1)
    linked_list.insert(0)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.remove_node(3)
    # 1 2 3
    linked_list.traverse_forward()

    # 3 2 1
    linked_list.traverse_backward()
