#----------------------------------------------------------------------
#This is the base file for binary trees. I wouldn't reccommend using it 
#barebones, at least use something like binary_search_tree.py. 

#binaryTree is (somewhat obviously) the most basic version of any
#tree in this folder, thus it's not super useful... it's really just
#here as a composite pattern (at least I think that's what it's called)

#All subclasses (binary_search_tree.py, etc.) will need (at least) an 
#insert function and a delete function to work properly!
#----------------------------------------------------------------------

from queues.queue import Queue as q
from collections import defaultdict

#contains different types of trees, such as a complete binary tree, a perfect binary tree, etc.
class Node:

    #nodes have their key and an optional lower right and left 
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None


        
class BinaryTree:

    def __init__(self, root=None) -> None:
        self.root = root
    
    #------------------
    #Printing the tree
    #------------------

    def print_tree(self) -> None:
        #nodes seperated into levels, not in order though
        level_info = defaultdict(list)
        level_info = self.collect_level_info(self.root, level_info, 0)

        #removing that annoying little "defaultdict" thingy
        level_info = dict(level_info)
        print(level_info)


    #function for print_tree(), takes the trees root as input
    def collect_level_info(self, root: Node, level_info=defaultdict(list), level=0) -> dict:
        #traverse the tree in a way that we can count the levels
        if root is not None:
            level_info[level].append(root.key)
            self.collect_level_info(root.left, level_info, level + 1)
            self.collect_level_info(root.right, level_info, level + 1)
            
        return level_info

    #------------------
    #Traversals
    #------------------

    def level_order_traversal(self) -> list:
        return self.level_order_traversal_helper(self.root)

    #technically jsut BFS, takes the trees root as input
    def level_order_traversal_helper(self, root: Node) -> list:
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
    

    def pre_order_traversal(self) -> list:
        return self.pre_order_traversal_helper(self.root)

    #visited contains the order that the nodes were traversed in
    #takes tree root and empty list as input
    def pre_order_traversal_helper(self, root: Node, visited=[]) -> list:
        if root:
            #"traverse" the root
            visited.append(root.key)
            #traverse left
            self.pre_order_dfs_traversal_helper(root.left, visited)
            #traverse right
            self.pre_order_dfs_traversal_helper(root.right, visited)

        return visited


    def post_order_traversal(self) -> list:
        return self.post_order_traversal_helper(self.root)

    #takes tree root and empty list as input
    def post_order_traversal_helper(self, root: Node, visited=[]) -> list:
        if root:
            #traverse left
            self.post_order_traversal_helper(root.left, visited)
            #traverse right
            self.post_order_traversal_helper(root.right, visited)
            #"traverse" the root
            visited.append(root.key)

        return visited


    def in_order_traversal(self) -> list:
        return self.in_order_traversal_helper(self.root)

    #takes tree root and empty list as input
    def in_order_traversal_helper(self, root: Node, visited=[], check_for_full=False, total_node_count=0) -> list | bool:
        if check_for_full:
            if root.left and not root.right:
                total_node_count -= 1

            elif root.right and not root.left:
                total_node_count -= 1

        if root:
            #traverse left
            self.in_order_traversal_helper(root.left, visited, check_for_full, total_node_count)
            #"traverse" the root
            visited.append(root.key)
            #traverse right
            self.in_order_traversal_helper(root.right, visited, check_for_full, total_node_count)

        total_node_count += 1
        
        return len(visited) == total_node_count

    #------------------------------------------------
    #Functions for general information about the tree
    #------------------------------------------------

    #depth of the TREE, not a certain node
    def find_tree_depth(self) -> int:
        return self.find_tree_depth_helper(self.root)

    def find_tree_depth_helper(self, root: Node) -> int:
        #init the depth to 0
        d = 0
        #go straight down the left side
        while root != None:
            d += 1
            root = root.left

        return d
    

    #height of the TREE, not a certain node
    def find_tree_height(self) -> int:
        return self.find_tree_height_helper(self.root)

    def find_tree_height_helper(self, root: Node) -> int:
        #if no tree
        if not root:
            return 0
        
        #if we're at the bottom
        if not root.left and not root.right:
            return 0
        
        #recursive calls
        leftHeight = self.find_tree_height_helper(root.left)
        rightHeight = self.find_tree_height_helper(root.right)
        if leftHeight > rightHeight:
            return leftHeight + 1
        
        else:
            return rightHeight + 1

    #-----------------------------------------------------------
    #Functions for state of tree (complete, full, balanced, etc) 
    #-----------------------------------------------------------

    def is_full_binary_tree(self) -> bool:
        res = self.is_full_binary_tree_helper(self.root)
        if type(res) == list:
            return False
        
        return res
    
    #keep in mind we're trying to find a node with only one child (to return false)
    def is_full_binary_tree_helper(self, root: Node) -> bool:
        #if no root, its a full tree
        if not root:
            return True

        #if no nodes on both sides
        if not root.left and not root.right:
            return True

        #recurse on both sides
        if root.left and root.right:
            return self.is_full_binary_tree_helper(root.left) and self.is_full_binary_tree_helper(root.left)

        return False
    

    def is_perfect_binary_tree(self) -> bool:
        '''
        this was the function that i wrote with no help, just keeping it around :)

        level_order_nodes = self.collect_level_info(self.root)

        count = 2
        for k in level_order_nodes.keys():
            if len(level_order_nodes[k])*2 != count:
                return False
            
            count *= 2

        return True
        '''
        d = self.find_tree_depth()
        return self.is_perfect_binary_tree_helper(self.root, d)

    def is_perfect_binary_tree_helper(self, root:Node, d, level=0) -> bool:
        #empty tree is perfect
        if not root:
            return True
        
        #if leaf node, then its depth must be = all other leaves depth
        if not root.left and not root.right:
            return (d == level + 1) 
        
        #if internal node and one child is empty
        if not root.left or not root.right:
            return False
        
        #left and right subtrees must be perfect
        return self.is_perfect_binary_tree_helper(root.left, d, level+1) and self.is_perfect_binary_tree_helper(root.right, d, level+1) 



if __name__ == "__main__":
    pass




