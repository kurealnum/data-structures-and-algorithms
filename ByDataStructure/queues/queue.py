#NOTE: you don't *have* to use a Llist for queues (technically speaking)
#importing my linked list file
#when you print/interact with the queue, the newest/value closest to the end is the leftmost value

#imports
import linked_lists.singlylinkedlist as ll

#the head and end of the list should always be null
MAX_LENGTH = 10
input_queue = [1, 2, 3, 4, 5]

class queue():

    def __init__(self, input_queue, max_length) -> None:
        self.max_length = max_length

        #filling up the queue
        self.queue_array = ll.linked_list()
        self.queue_array.fill_llist(input_queue)


    #returns true if the queue is full
    def isFull(self):
        length = self.queue_array.len_of_llist()
        if length[1] + 1 > MAX_LENGTH:
            return True
        
        return False


    #returns true if the queue is empty
    def isEmpty(self):
        length = self.queue_array.len_of_llist()
        if length[1] == 0:
            return True

        return False


    #returns false if the queue is full, returns nothing if it works
    def enqueue(self, value):
        if self.isFull():
            return False
        
        self.queue_array.insert_item_head(ll.node(value))


    #returns false if the queue is empty, nothing if it works
    def dequeue(self):
        length = self.queue_array.len_of_llist()
        if self.isEmpty():
            return False
        
        #-1 is because the length returns the length of a 1 indexed array
        self.queue_array.remove_item(length[1]-1)
        

    #returns the object at the front of the queue(the head)
    def front(self):
        return self.queue_array.head.value


    #returns the object at the end of the queue
    def rear(self):
        return self.queue_array.find_item(self.queue_array.len_of_llist()[1]-1)
    

    def print_queue(self):
        self.queue_array.printList()


if __name__ == "__main__":
    queue_1 = queue(input_queue, MAX_LENGTH)
    queue_1.print_queue()


