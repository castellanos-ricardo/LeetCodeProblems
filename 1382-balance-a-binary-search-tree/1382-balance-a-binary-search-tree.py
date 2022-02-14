# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sortedList = self.inOrderDfs(root)
        return self.buildBST(sortedList)
        
        
    def inOrderDfs(self,root):
        if not root:
            return []
        return self.inOrderDfs(root.left)+[root.val]+self.inOrderDfs(root.right)
    
    def buildBST(self,sortedList):
        if not sortedList:
            return None
        
        m = 0+(len(sortedList)-1)//2
        root = TreeNode(sortedList[m])
        root.left = self.buildBST(sortedList[:m])
        root.right = self.buildBST(sortedList[m+1:])
        return root        
        
        
        
        
            
    