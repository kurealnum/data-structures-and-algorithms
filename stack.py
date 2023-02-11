#importing my linked list file
import sys
sys.path.append('C:\Code\Python\Data Structures')

#imports
import singlylinkedlist as ll
llist = ll.linked_list()

#just to start something off
stack = [1, 2, 3, 4, 5]
llist.fill_llist(stack)

#put an item on top of the stack, takes one arg, value. can be int or str
def push_stack(value):
    llist.insert_item_head(ll.node(value))



#pop an item on top of the stack
def pop_stack():
    llist.remove_item(0)



#returns the top of the stack
def top_of_stack():
    return llist.head.value



#checks if the stack is empty, returns true if it is, false if it isn't
def is_stack_empty():
    data = llist.len_of_llist()
    if data[0] == False:
        return True
    
    return False



#returns the size of the stack
def size_of_stack():
    data = llist.len_of_llist()
    if data[0] == False:
        return 0
    
    return data[1]

    

llist.printList()
print(size_of_stack())
llist.printList()
      




