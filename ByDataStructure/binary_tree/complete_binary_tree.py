import queues.queue
import linked_lists.singlylinkedlist as ll

#contains different types of trees, such as a complete binary tree, a perfect binary tree, etc.
class node:

    #nodes have their data and an optional lower right and left 
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


        
class binarytree:

    def __init__(self, root) -> None:
        self.root = root
        #level info is for printing
        self.level_info = {}

    #a completely binary tree is a full binary tree, 
    #but all leaf elements must lean towards the left, 
    #and the last leaf element might not have a right sibling
    #(i.e. a complete binary tree doesn't have to be a full binary tree)
    def fill_tree(self, root, list=list):
        #loop through the list
        for i in list:
            self.insert(root, node(i))


    def insert(self, root, node):
        #if the root is none, just set the node to the root

        #maybe check the actual root, not the arg
        if self.root is None:
            self.root = node

        #if it isn't (it won't be most times of course)
        else:
            #if the root is smaller than the node, we go down the right side
            if root.data < node.data:
                #if there's nothing in the right node, put the node there
                if root.right is None:
                    root.right = node
                
                #if there is, go ahead and recursively call the function again,
                #this time having the root set as the right node
                else: 
                    self.insert(root.right, node)

            #if the root is bigger than the node, we go down the left side
            elif root.data > node.data:
                #if there's nothing in the left node, put the node there
                if root.left is None:
                    root.left = node

                #if there is, recursively call the function again with the "root"
                #argument set as the left node that we're currently on
                else: 
                    self.insert(root.left, node)

            #if the root is equal to the current node
            else:
                #worst comes to worst, we just put it in the left node
                if root.left is None:
                    root.left = node

                #if there is something in the left node, go check that out
                else:
                    self.insert(root.left, node)


    def bfs_traversal(self):
        llist = ll.linked_list()
        
        queue = []
        visited = []


    def print_tree(self, root, level):
        if root is not None:
            self.print_tree(root.right, level + 1)
            print(level, str(root.data))
            self.print_tree(root.left, level + 1)
                    


#nums list to fill the tree with
nums = [2, 3, 4, 5, 6, 1, 7]
#sorting it
#nums = sorted(nums)

#this is the middle of the list (rounded down)
mid = int(len(nums) // 2)

#setting the root (which is the middle)
root = node(nums[mid])
print(f'Root: {root.data}')
#removing what we set as the root so we don't have a duplicate root
nums.pop(mid)

#our main class to do everything out of, so it's nice and organized
bt = binarytree(root)

bt.fill_tree(root, nums)
bt.insert(root, node(8))
bt.print_tree(root, 0)






