import queues.queue as q
from collections import defaultdict

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
        self.node_count = 1 

    #a completel binary tree is a full binary tree, 
    #but all leaf elements must lean towards the left, 
    #and the last leaf element might not have a right sibling
    #(i.e. a complete binary tree doesn't have to be a full binary tree)
    def fill_tree(self, root, list=list):
        self.input_array = list
        
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
                    self.node_count += 1
                
                #if there is, go ahead and recursively call the function again,
                #this time having the root set as the right node
                else: 
                    self.insert(root.right, node)

            #if the root is bigger than the node, we go down the left side
            elif root.data > node.data:
                #if there's nothing in the left node, put the node there
                if root.left is None:
                    root.left = node
                    self.node_count += 1

                #if there is, recursively call the function again with the "root"
                #argument set as the left node that we're currently on
                else: 
                    self.insert(root.left, node)

            #if the root is equal to the current node
            else:
                #worst comes to worst, we just put it in the left node
                if root.left is None:
                    root.left = node
                    self.node_count += 1

                #if there is something in the left node, go check that out
                else:
                    self.insert(root.left, node)
    

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


    #function for print_tree()
    def collect_level_info(self, root, level_info=defaultdict(list), level=0):
        #traverse the tree in a way that we can count the levels
        if root is not None:
            self.collect_level_info(root.left, level_info, level + 1)
            level_info[level].append(root.data)
            self.collect_level_info(root.right, level_info, level + 1)
            
                    
        return level_info


    def bfs_traversal(self, root):
        #0 sets the max queue length to inf
        queue = q.queue([],0)
        queue.enqueue(root)
        #visited (in order)
        visited = []

        while not queue.isEmpty():
            #set current node as last element of q, pop last element of q
            currentNode = queue.dequeue()
            visited.append(currentNode.data)

            #if this node isn't none
            if currentNode.left:
                queue.enqueue(currentNode.left)

            #if this node isn't none
            if currentNode.right:
                queue.enqueue(currentNode.right)
            
        return visited
    

    #visited contains the order that the nodes were traversed in
    def pre_order_traversal(self, root, visited):
        if root:
            #"traverse" the root
            visited.append(root.data)
            #traverse left
            self.pre_order_dfs_traversal(root.left, visited)
            #traverse right
            self.pre_order_dfs_traversal(root.right, visited)


    def post_order_traversal(self, root, visited):
        if root:
            #traverse left
            self.post_order_traversal(root.left, visited)
            #traverse right
            self.post_order_traversal(root.right, visited)
            #"traverse" the root
            visited.append(root.data)


    def in_order_traversal(self, root, visited):
        if root:
            #traverse left
            self.in_order_traversal(root.left,visited)
            #"traverse" the root
            visited.append(root.data)
            #traverse right
            self.in_order_traversal(root.right,visited)


    #TBD stands for To Be Deleted
    def delete_node(self, root, k):
        #base case
        if root is None:
            return root
    
        #recursive calls for ancestors of
        #node to be deleted
        if root.data > k:
            root.left = self.delete_node(root.left, k)
            return root
        elif root.data < k:
            root.right = self.delete_node(root.right, k)
            return root
    
        #we reach here when root is the node to be deleted.
    
        #if one of the children is empty
        if root.left is None:
            temp = root.right
            del root
            return temp
        elif root.right is None:
            temp = root.left
            del root
            return temp
    
        #if both children exist
        else:
    
            succParent = root
    
            #find successor
            succ = root.right
            while succ.left is not None:
                succParent = succ
                succ = succ.left
    
            #Delete successor. Since successor is always left child of its parent 
            #we can safely make successor's right right child as left of its parent. If 
            #there is no succ, then assign succ.right to succParent.right
            if succParent != root:
                succParent.left = succ.right
            else:
                succParent.right = succ.right
    
            #copy Successor Data to root
            root.data = succ.data
    
            #delete Successor and return root
            del succ
            return root



if __name__ == "__main__":
    #init stuff-----------
    #nums list to fill the tree with
    nums = [2, 3, 4, 5, 6, 1, 7]
    

    mid = int(len(nums) // 2)

    #setting the root (which is the middle)
    root = node(nums[mid])
    nums.pop(mid)

    bt = binarytree(root)

    bt.fill_tree(root, nums)
    #end of init stuff-----------

    bt.print_tree()
    bt.delete_node(bt.root, 2)

    bt.print_tree()








