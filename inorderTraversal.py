# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        nodes = []
        self.inorderTraversalHelper(root, nodes)
        return nodes
    
    def inorderTraversalHelper(self, root, nodes):
        if root is None:
            return
        # left, self, right
        self.inorderTraversalHelper(root.left, nodes)
        nodes.append(root.val)
        self.inorderTraversalHelper(root.right, nodes)
    
        
        