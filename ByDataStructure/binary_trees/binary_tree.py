#----------------------------------------------------------------------
#This is the base file for binary trees. I wouldn't reccommend using it 
#barebones, at least use something like binary_search_tree.py. 

#binary_tree is (somewhat obviously) the most basic version of any
#tree in this folder, thus it's not super useful... it's really just
#here as a composite pattern (at least I think that's what it's called)
#----------------------------------------------------------------------

import queues.queue as q
from collections import defaultdict

#contains different types of trees, such as a complete binary tree, a perfect binary tree, etc.
class node:

    #nodes have their key and an optional lower right and left 
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None


        
class binary_tree:

    def __init__(self, root=None) -> None:
        self.root = root
        self.node_count = 1 

    #------------------
    #2 methods of filling trees
    #------------------

    #a completel binary tree is a full binary tree, 
    #but all leaf elements must lean towards the left, 
    #and the last leaf element might not have a right sibling
    #(i.e. a complete binary tree doesn't have to be a full binary tree)
    def fill_tree(self, root, list=list):
        self.input_array = list
        
        #loop through the list
        for i in list:
            self.insert(root, node(i))


    #takes a sorted array as input. use with caution, will partially 
    #overwrite current tree if input array is != current # of nodes 

    #IMPORTANT!!! when you run this, set the binary trees root = this 
    #function (i.e. the return value of this func)
    def fill_balanced_tree(self, arr):
        if not arr:
            return None

        mid = len(arr) // 2

        root = node(arr[mid])

        root.left = self.fill_balanced_tree(arr[:mid])
        root.right = self.fill_balanced_tree(arr[mid+1:])

        return root
    
    #------------------
    #Printing the tree
    #------------------

    def print_tree(self):
        #nodes seperated into levels, not in order though
        level_info = defaultdict(list)
        level_info = self.collect_level_info(self.root, level_info, 0)

        #sorting the dict for ease of access or whatever you call it
        level_info_keys = list(level_info.keys())
        level_info_keys.sort()
        level_info = {i: level_info[i] for i in level_info_keys}

        #nodes in order from top to bottom, left to right (BFS). 
        #keys = level, level index from 0
        print(level_info)


    #function for print_tree(), takes the trees root as input
    def collect_level_info(self, root, level_info=defaultdict(list), level=0):
        #traverse the tree in a way that we can count the levels
        if root is not None:
            self.collect_level_info(root.left, level_info, level + 1)
            level_info[level].append(root.key)
            self.collect_level_info(root.right, level_info, level + 1)
            
                    
        return level_info

    #------------------
    #Traversals
    #------------------

    #technically jsut BFS, takes the trees root as input
    def level_order_traversal(self, root):
        #0 sets the max queue length to inf
        queue = q.queue([],0)
        queue.enqueue(root)
        #visited (in order)
        visited = []

        while not queue.isEmpty():
            #set current node as last element of q, pop last element of q
            currentNode = queue.dequeue()
            visited.append(currentNode.key)

            #if this node isn't none
            if currentNode.left:
                queue.enqueue(currentNode.left)

            #if this node isn't none
            if currentNode.right:
                queue.enqueue(currentNode.right)
            
        return visited
    

    #visited contains the order that the nodes were traversed in
    #takes tree root and empty list as input
    def pre_order_traversal(self, root, visited=[]):
        if root:
            #"traverse" the root
            visited.append(root.key)
            #traverse left
            self.pre_order_dfs_traversal(root.left, visited)
            #traverse right
            self.pre_order_dfs_traversal(root.right, visited)

        return visited


    #takes tree root and empty list as input
    def post_order_traversal(self, root, visited=[]):
        if root:
            #traverse left
            self.post_order_traversal(root.left, visited)
            #traverse right
            self.post_order_traversal(root.right, visited)
            #"traverse" the root
            visited.append(root.key)

        return visited


    #takes tree root and empty list as input
    def in_order_traversal(self, root, visited=[]):
        if root:
            #traverse left
            self.in_order_traversal(root.left,visited)
            #"traverse" the root
            visited.append(root.key)
            #traverse right
            self.in_order_traversal(root.right,visited)

        return visited
    
    #------------------



if __name__ == "__main__":
    #init stuff-----------
    #nums list to fill the tree with
    nums = [1,2,3,4,5,6,7]
    

    mid = int(len(nums) // 2)

    #setting the root (which is the middle)
    root = node(nums[mid])
    nums.pop(mid)

    bt = binary_tree(root)
    bt.fill_tree(bt.root,nums)
    #end of init stuff-----------

   
    
    nodes_in_order = [1,2,3,4,5,6,7]
    bt.fill_balanced_tree(nodes_in_order)
    bt.root = bt.fill_balanced_tree(nodes_in_order)

    bt.print_tree()
    print(bt.in_order_traversal(bt.root))







