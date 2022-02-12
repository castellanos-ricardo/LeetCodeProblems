# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp = TreeNode(val)
        if not root:
            return temp
        
        current = root
        while root:
            if val>current.val:
                if not current.right:
                    current.right = temp
                    break
                current = current.right
            else:
                if not current.left:
                    current.left = temp
                    break
                current = current.left
        return root
        
    
#     def breadthFirstTraversal(self, root):
#         queue = [root]
#         res = []
#         while queue:
#             current = queue.pop(0)
#             if current:
#                 res += [current.val]
#                 queue +=[current.left, current.right]
#         return res
            
            
            
        
        