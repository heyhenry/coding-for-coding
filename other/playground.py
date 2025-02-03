# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root

    def next(self) -> int:
        return self.root.right

    def hasNext(self) -> bool:
        if self.root.right is not None:
            return True
        return False

# Input BST (constructed manually)
root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

# Initialize iterator
iterator = BSTIterator(root)

# Expected Output
print(iterator.next())    # 3
print(iterator.next())    # 7
print(iterator.hasNext()) # True
print(iterator.next())    # 9
print(iterator.hasNext()) # True
print(iterator.next())    # 15
print(iterator.hasNext()) # True
print(iterator.next())    # 20
print(iterator.hasNext()) # False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()