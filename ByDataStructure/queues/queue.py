#-----------------------------------------------
#Basic queue data structure. You don't *have to*
#use a linked list, but I think it's a nice
#demonstration. When you print/interact with the
#queue, the leftmost value is the one closest to
#the end.
#-----------------------------------------------

#imports
import linked_lists.singlylinkedlist as ll
from math import inf

class queue():

    def __init__(self, input_queue, max_length) -> None:
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
    def isFull(self):
        length = self.queue_array.len_of_llist()
        if length[1] + 1 > self.max_length:
            return True
        
        return False


    #returns true if the queue is empty, false if it isnt
    def isEmpty(self):
        length = self.queue_array.len_of_llist()
        if length[1] == 0:
            return True

        return False
    

    #returns the object at the front of the queue(the head), return 
    #option for the value defaults to true
    def front(self, value):
        #return the node with the value if true
        if value:
            return self.queue_array.head.value
        
        return self.queue_array.head


    #returns the object at the end of the queue, return 
    #option for the value defaults to true
    def rear(self, value=True):
        if value:
            return self.queue_array.find_item(self.queue_array.len_of_llist()[1]-1).value
        
        #return the node with the value if true
        return self.queue_array.find_item(self.queue_array.len_of_llist()[1]-1)
    

    #literally just prints the queue
    def print_queue(self):
        self.queue_array.print_list()

    #----------------
    #Enqueue/dequeue
    #----------------

    #raises exception if the queue is full, returns nothing if it works
    def enqueue(self, value):
        if self.isFull():
            raise Exception("Error in queue.enqueue: Queue is full, no room to insert")
        
        self.queue_array.insert_item_head(ll.node(value))


    #returns false if the queue is empty, nothing if it works
    def dequeue(self):
        length = self.queue_array.len_of_llist()
        if self.isEmpty():
            return None
        
        #-1 is because the length returns the length of a 1 indexed array
        return self.queue_array.pop_item(length[1]-1)
    


if __name__ == "__main__":
    #input a 0 to set the maxlength of the queue to infinity
    MAX_LENGTH = 0
    input_queue = [1, 2, 3, 4, 5]

    queue_1 = queue(input_queue, MAX_LENGTH)
    queue_1.print_queue()
    print(queue_1.dequeue())
    queue_1.print_queue()


