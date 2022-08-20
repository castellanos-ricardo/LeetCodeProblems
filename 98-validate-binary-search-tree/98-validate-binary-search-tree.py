# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#the key to this problem is updating the left and right of x < current.val < y
#we start with -inf < x < inf
#since the root of binary tree has no boundries in order to be valid

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root,float("-inf"),float("inf"))
    
    def dfs(self,node, left, right):
        if not node:
            return True
        if not (left < node.val < right):
            return False
        
        return self.dfs(node.left,left,node.val) and self.dfs(node.right,node.val,right)