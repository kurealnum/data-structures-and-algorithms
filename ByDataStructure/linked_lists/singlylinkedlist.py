class node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class linked_list:
    
    def __init__(self) -> None:
        self.head = None

    def printList(self):
        #start at the head
        temp = self.head
        count = 0
        node = self.head
        #while there's stuff inside of temp
        while node:
            count += 1
            node = node.next
            
        while (temp):
            # If it's not the last node, print the arrow
            if count > 1:
                print(temp.value, end=' --> ')
                count -= 1
            # If it's the last node, don't print the arrow
            else:
                print(temp.value)
                
            temp = temp.next


    #populate the list with whatever list you want
    def fill_llist(self, list=list):
        #putting the directions into the linked list
        if self.head == None:
            head = node(list[0])
            self.head = head
            
        current = head

        #loop through the list, starting 1 index into the list
        #we're using "i" because the list could contain anything, just makes it more readable
        for i in list[1:]:
            #define a temporary new node
            value = node(i)

            #set the next variable to the temporary node
            current.next = value

            #set the current node to the temporary node
            current = value


    #takes a string as an arg, not a node
    def find_item(self, find_val):

        count = 0

        #we always name the current variable "current", because we don't really have a traditional index, so to speak
        current = self.head

        while current:
            #if the values are equivalent 
            if count == find_val or current.value == find_val:
                return current.value
            
            current = current.next
            count += 1

        else:
            print(f'Couldn\'t find {find_val}') 


    #takes a node as an argument
    def insert_item_head(self, new_head):
        #set the point variable in the old head to the pointer in the new head
        new_head.next = self.head
        #make the old head = the new head
        self.head = new_head


    #takes node as arg
    def insert_item_end(self, new_end):
        #set the current var
        current = self.head

        #if we don't have anything in the list, go ahead and make a new head with the node we want
        if self.head is None:
            self.head = new_end

        #keep going through the entire list
        while current:
            if current.next == None:
                #set the new end as the new node 
                current.next = new_end
                return

            #update the current var
            current = current.next


    '''
    inserts at the position (the iterator, technically)
    takes a node and a STRING OR INT as args, not a node and a node
    very similar to insert_item_by_name()
    if you want to access the head, you NEED to use an iterator
    '''
    def insert_item(self, value, position):
        if self.head is None:
            self.head = value

        current = self.head
        count = 1

        if position == 0 or position == self.head:
            value.next = self.head
            self.head = value
            return

        while current:
            #basically just normal python lists, but over engineered 
            if count == position or current.value == position:
                value.next = current.next
                current.next = value
                return

            current = current.next
            count += 1

        print(f"Out of index/couldn't find variable to insert after: {value.value}")


    #takes an int OR a string as an argument (i.e. deletes item either by iterator or name)
    def pop_item(self, position):
        count = 0
        current = self.head
        previous = None
        
        #just basic iteration, only this time we're using a previous variable to keep track of where we were
        while current:
            if count == position or current.value == position:
                if previous:
                    previous.next = current.next         
                else: 
                    self.head = current.next
                    
                #the removed node
                return current.value
           
            previous = current
            current = current.next
            count += 1

        return False
    

    #takes no args, just returns a set (True/False, and the length of the linked list)
    def len_of_llist(self):
        #go ahead and check if there's nothing in there
        if self.head == None:
            return False, 0
        
        #if there is, loop through and count the length
        count = 0
        current = self.head
        
        while current:
            count += 1
            current = current.next 

        return True, count

        
llist = linked_list()
directions = ['Go straight', 'Turn left', "Turn right", "Stop", "Park"]

if __name__ == "main":
    llist.fill_llist(directions)
    print(llist.len_of_llist())
    llist.printList()

