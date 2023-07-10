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

        #sorting the dict for ease of access or whatever you call it
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


    
    #-----------------------------------------------------------
    #Functions for state of tree (complete, full, balanced, etc) 
    #-----------------------------------------------------------

    def is_full_binary_tree(self):
        res = self.is_full_binary_tree_helper(self.root)
        if type(res) == list:
            return False
        
        return res
    

    def is_full_binary_tree_helper(self, root: Node):
        if not root:
            return True

        if not root.left and not root.right:
            return True

        if root.left and root.right:
            return self.is_full_binary_tree_helper(root.left) and self.is_full_binary_tree_helper(root.left)

        return False
    

    def is_perfect_binary_tree(self):
        pass


    def is_perfect_binary_tree_helper(self):
        pass



if __name__ == "__main__":
    pass




