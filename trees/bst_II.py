# round two of the same thing as bst_I

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, val):
        if val < self.value:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)

tree = TreeNode(10)
tree.insert(5)
tree.insert(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(22)
tree.insert(11)
tree.insert(12)