from binary_tree import Node, BinaryTree

#inherits all properties from node
class Node(Node):
    pass



#binary search trees are pretty much just binary trees, thus its smooth inheritance
class BinarySearchTree(BinaryTree):

    #------------------
    #2 methods of filling trees
    #------------------

    #a complete binary tree is a full binary tree, 
    #but all leaf elements must lean towards the left, 
    #and the last leaf element might not have a right sibling
    #(i.e. a complete binary tree doesn't have to be a full binary tree)
    def fill_tree(self, root, list=list):
        self.input_array = list
        
        #loop through the list
        for i in list:
            self.insert(root, Node(i))


    #takes a sorted array as input. use with caution, will partially 
    #overwrite current tree if input array is != current # of nodes 

    #IMPORTANT!!! when you run this, set the binary trees root = this 
    #function (i.e. the return value of this func)
    def fill_balanced_tree(self, arr):
        if not arr:
            return None

        mid = len(arr) // 2

        root = Node(arr[mid])

        root.left = self.fill_balanced_tree(arr[:mid])
        root.right = self.fill_balanced_tree(arr[mid+1:])

        return root
    
    #-------------------------------
    #Insert/delete/search functions
    #-------------------------------

    #this is here so you don't have to add "bst.root" to the func call
    def search(self, target_value):
        return self.search_helper(target_value, self.root)


    #make sure to add .key to whatever return value you get, as this just returns the node objec t
    def search_helper(self, target_value, node):
        current = node.key
        if target_value == current:
            return node
        
        if target_value > current:
            return self.search_helper(target_value, node.right)

        else:
            return self.search_helper(target_value, node.left)


    #takes the root and a new node() object as input
    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root


    #TBD stands for To Be Deleted, takes tree root and new node *value* as input
    def delete_node_helper(self, root):
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
    
            #copy Successor key to root
            root.key = succ.key
    
            #delete Successor and return root
            del succ
            return root
        

    def delete(self, target_node):
        node = self.search(target_node)
        self.delete_node_helper(node)




if __name__ == "__main__":
    root = Node(4)
    bst = BinarySearchTree(root)
    
    nodes_in_order = [1,2,3,4,5,6,7]
    bst.root = bst.fill_balanced_tree(nodes_in_order)

    bst.print_tree()
    bst.delete(3)
    print(bst.search(3))
    bst.print_tree()

