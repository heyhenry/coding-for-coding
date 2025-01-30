# rule of binary search tree 

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # insert the value either left or right of a tree node, 
    # based on its availability and value
    def insert(self, value):
        # the value is shown to be larger than the current tree node's value
        if value < self.value:
            # check if the left spot is available in the treenode
            # if so, take that spot
            if self.left is None:
                self.left = TreeNode(value)
            # if it isn't available, search the next left treenode and so on
            # until you find an available spot (which could also be on the right side during a new insert call!)
            else:
                self.left.insert(value)
        else:
            # since the value's actually bigger than the current tree node,
            # check if the right spot is available
            if self.right is None:
                self.right = TreeNode(value)
            # if the right spot isn't available, 
            # check the next right spot by calling insert() again and it'll search the right spot's node values
            else:
                self.right.insert(value)

    # prints from smallest to largest
    def inorder_traversal(self):
        # goes down the left side until it can't,
        # then prints the last node it traversed
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        # after all the left side's nodes values are logged,
        # it'll check the right side values and find the lowest
        # and continue printing until all the right side nodes are logged
        if self.right:
            self.right.inorder_traversal()

    # Preorder Traversal:
    # - The current node is printed first.
    # - The traversal starts from the leftmost node and moves right.
    # - Each subtree follows the same pattern (Root → Left → Right).
    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    # Preorder Traversal:
    # - The current node is printed first.
    # - The traversal starts from the leftmost node and moves right.
    # - Each subtree follows the same pattern (Root → Left → Right).
    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)

tree = TreeNode(10)
tree.insert(5)
tree.insert(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(22)
tree.insert(11)
tree.insert(12)

# tree.inorder_traversal()
tree.preorder_traversal()
# tree.postorder_traversal()