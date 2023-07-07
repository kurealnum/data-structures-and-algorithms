#-----------------------------------------------
#Generic stack data structure. You don't *have*
#to use a Llist for stacks (technically speaking)
#-----------------------------------------------

#importing my linked list file
from linked_lists.singlylinkedlist import LinkedList as ll

#just to start something off
stack = [1, 2, 3, 4, 5]

class Stack():

    def __init__(self, stack) -> None:
        #filling up the stack
        self.stack_array = ll.linked_list()
        self.stack_array.fill_llist(stack)

    #------------------
    #General functions
    #------------------

    #returns the top of the stack
    def top_of_stack(self):
        return self.stack_array.head.value


    #checks if the stack is empty, returns true if it is, false if it isn't
    def is_stack_empty(self):
        data = self.stack_array.len_of_llist()
        if data[0] == False:
            return True
        
        return False


    #returns the size of the stack
    def size_of_stack(self):
        data = self.stack_array.len_of_llist()
        return data[1]
    
    
    #literally just prints the stack
    def print_stack(self):
        self.stack_array.print_list()

    #----------------------
    #Push and pop functions
    #----------------------

    #put an item on top of the stack, takes one arg, value. can be int or str
    def push_stack(self, value):
        self.stack_array.insert_item_head(ll.node(value))


    #pop an item on top of the stack
    def pop_stack(self):
        self.stack_array.pop_item(0)



if __name__ == "__main__":
    pass
      




