from binary_tree import Node, BinaryTree

#inherits all properties from node
class Node(Node):
    pass



#binary search trees are pretty much just binary trees, thus its smooth inheritance
class BinarySearchTree(BinaryTree):
    
    #-----------------------
    #Insert/delete functions
    #-----------------------

    #takes the root and a new node() object as input
    def insert(self, root, node):
        #if the root is none, just set the node to the root

        #maybe check the actual root, not the arg
        if self.root is None:
            self.root = node

        #if it isn't (it won't be most times of course)
        else:
            #if the root is smaller than the node, we go down the right side
            if root.key < node.key:
                #if there's nothing in the right node, put the node there
                if root.right is None:
                    root.right = node
                    self.node_count += 1
                
                #if there is, go ahead and recursively call the function again,
                #this time having the root set as the right node
                else: 
                    self.insert(root.right, node)

            #if the root is bigger than the node, we go down the left side
            elif root.key > node.key:
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


    #TBD stands for To Be Deleted, takes tree root and new node *value* as input
    def delete_node(self, root, k):
        #base case
        if root is None:
            return root

        #recursive calls for ancestors of
        #node to be deleted
        if root.key > k:
            root.left = self.delete_node(root.left, k)
            return root
        elif root.key < k:
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
    
            #copy Successor key to root
            root.key = succ.key
    
            #delete Successor and return root
            del succ
            return root


if __name__ == "__main__":
    #init stuff-----------
    #nums list to fill the tree with
    nums = [1,2,3,4,5,6,7]
    

    mid = int(len(nums) // 2)

    #setting the root (which is the middle)
    root = Node(nums[mid])
    nums.pop(mid)

    bt = BinaryTree(root)
    bt.fill_tree(bt.root,nums)
    #end of init stuff-----------

   
    
    nodes_in_order = [1,2,3,4,5,6,7]
    bt.fill_balanced_tree(nodes_in_order)
    bt.root = bt.fill_balanced_tree(nodes_in_order)

    bt.print_tree()
    print(bt.in_order_traversal(bt.root))  


