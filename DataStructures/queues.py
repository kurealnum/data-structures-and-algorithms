#NOTE: you don't *have* to use a Llist for queues (technically speaking)
#importing my linked list file
#when you print/interact with the queue, the newest/value closest to the end is the leftmost value
import sys
sys.path.append('C:\Code\Python\Data Structures')

#imports
import singlylinkedlist as ll
llist = ll.linked_list()

#the head and end of the list should always be null
MAX_LENGTH = 10
queue = [1, 2, 3, 4, 5]
llist.fill_llist(queue)


#returns true if the queue is full
def isFull():
    length = llist.len_of_llist()
    if length[1] + 1 > MAX_LENGTH:
        return True
    
    return False
    

#returns true if the queue is empty
def isEmpty():
    length = llist.len_of_llist()
    if length[1] == 0:
        return True

    return False


#returns false if the queue is full, returns nothing if it works
def enqueue(value):
    length = llist.len_of_llist()
    if isFull():
        return False
    
    llist.insert_item_head(ll.node(value))


#returns false if the queue is empty, nothing if it works
def dequeue():
    length = llist.len_of_llist()
    if isEmpty():
        return False
    
    #i forget why i have to do the "-1" lol
    llist.remove_item(length[1]-1)
    

#returns the object at the front of the queue(the head)
def front():
    return llist.head.value


#returns the object at the end of the queue
def rear():
    return llist.find_item(llist.len_of_llist()[1]-1)


for i in reversed(range(5)):
    enqueue(i)
    dequeue()

llist.printList()