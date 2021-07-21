# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        isSameTree = self.traversal(p, q)
        return isSameTree
    
    def traversal(self, p, q):
        if p is None and q is not None or q is None and p is not None:
            return False
        elif p is None and q is None:
            return True
        else:
            if p.val == q.val:
                return self.traversal(p.left, q.left) and self.traversal(p.right, q.right)
            else:
                return False