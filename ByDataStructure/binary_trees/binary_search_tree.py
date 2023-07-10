from binary_tree import Node, BinaryTree

#inherits all properties from node
class Node(Node):
    pass



#binary search trees are pretty much just binary trees, thus its smooth inheritance
class BinarySearchTree(BinaryTree):

    #------------------
    #2 methods of filling trees
    #------------------

    def fill_tree(self, list: list) -> None:
        self.fill_tree_helper(self.root, list)

    def fill_tree_helper(self, root: Node, list=list):
        self.input_array = list
        
        #loop through the list
        for i in list:
            self.insert_helper(root, i)


    def fill_balanced_tree(self, arr: list) -> None:
        self.root = self.fill_balanced_tree_helper(arr)

    #takes a sorted array as input. use with caution, will partially 
    #overwrite current tree if input array is != current # of nodes 

    #IMPORTANT!!! when you run this, set the binary trees root = this 
    #function (i.e. the return value of this func)
    def fill_balanced_tree_helper(self, arr: list) -> Node:
        if not arr:
            return None

        mid = len(arr) // 2

        root = Node(arr[mid])

        root.left = self.fill_balanced_tree_helper(arr[:mid])
        root.right = self.fill_balanced_tree_helper(arr[mid+1:])

        return root
    
    #-------------------------------
    #Insert/remove/search functions
    #-------------------------------

    def search(self, target_node) -> Node:
        return self.search_helper(target_node, self.root)

    #make sure to add .key to whatever return value you get, as this just returns the node objec t
    def search_helper(self, target_node, node: Node) -> bool:
        current = node.key
        if target_node == current:
            return True
        
        if target_node > current:
            return self.search_helper(target_node, node.right)

        else:
            return self.search_helper(target_node, node.left)
        


    def insert(self, key) -> Node:
        self.insert_helper(self.root, key)

    #takes the root and a new node() object as input
    def insert_helper(self, root: Node, key) -> Node:
        if root is None:
            return Node(key)

        else:
            if root.key == key:
                return root
            elif root.key < key:
                root.right = self.insert_helper(root.right, key)
            else:
                root.left = self.insert_helper(root.left, key)

        return root


    def remove(self, target_node) -> Node:
        self.remove_node_helper(self.root, target_node)

    #TBD stands for To Be Removed, takes tree root and new node *value* as input
    def remove_node_helper(self, root: Node, node_TBD) -> Node:
        #finding the node TBD
        if not root:
            return root
        
        if node_TBD > root.key:
            #assign it incase it changes
            root.right = self.remove_node_helper(root.right, node_TBD)
            return root

        if node_TBD < root.key:
            #assign it incase it changes
            root.left = self.remove_node_helper(root.left, node_TBD)
            return root

        #deletion process
        else:
            #Case 1
            if not root.left:
                return root.right
            
            elif not root.right:
                return root.left
            
            #min from the right subtree, also case 2 and 3
            cur = root.right
            while cur.left:
                cur = cur.left

            root.key = cur.key
            #assign it to the right subtree in case it ends up changing
            root.right = self.remove_node_helper(root.right, root.key)
            return root



if __name__ == "__main__":
    root = Node(4)
    bst = BinarySearchTree(root)
    
    nodes_in_order = [1,2,3,4,5,6,7]
    bst.fill_tree(nodes_in_order)
    bst.print_tree()
    print(bst.is_perfect_binary_tree())

    

