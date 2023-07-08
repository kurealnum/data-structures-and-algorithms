#-----------------------------------------------
#Basic queue data structure. You don't *have to*
#use a linked list, but I think it's a nice
#demonstration. When you print/interact with the
#queue, the leftmost value is the one closest to
#the end.
#-----------------------------------------------

#imports
from linked_lists.singly_linked_list import LinkedList as ll
from linked_lists.singly_linked_list import Node
from math import inf

class Queue():

    #input a max length of 0 to set the max_length to infinity
    def __init__(self, input_queue: list, max_length: NotImplemented) -> None:
        self.max_length = max_length
        if self.max_length == 0:
            self.max_length = inf

        #creating the queue
        self.queue_array = ll.linked_list()

        #only fill if theres anything in there
        if len(input_queue) > 0:
            self.queue_array.fill_llist(input_queue)

    #-----------------
    #General functions
    #-----------------

    #returns true if the queue is full, false if it isnt
    def isFull(self) -> bool:
        length = self.queue_array.len_of_llist()
        if length[1] + 1 > self.max_length:
            return True
        
        return False


    #returns true if the queue is empty, false if it isnt
    def isEmpty(self) -> bool:
        length = self.queue_array.len_of_llist()
        if length[1] == 0:
            return True

        return False
    

    #returns the object at the front of the queue(the head), return 
    #option for the value defaults to true
    def front(self) -> Node:
        #return the node with the value if true
        return self.queue_array.head


    #returns the object at the end of the queue, return 
    #option for the value defaults to true
    def rear(self) -> Node:        
        #return the node with the value if true
        return self.queue_array.find_item(self.queue_array.len_of_llist()[1]-1)
    

    #literally just prints the queue
    def print_queue(self) -> None:
        self.queue_array.print_list()

    #----------------
    #Enqueue/dequeue
    #----------------

    #raises exception if the queue is full, returns nothing if it works
    def enqueue(self, value) -> None:
        if self.isFull():
            return None
        
        self.queue_array.insert_item_head(ll.node(value))


    def dequeue(self) -> None | Node:
        length = self.queue_array.len_of_llist()
        if self.isEmpty():
            return None
        
        #-1 is because the length returns the length of a 1 indexed array
        return self.queue_array.pop_item(length[1]-1)
    


if __name__ == "__main__":
    pass


