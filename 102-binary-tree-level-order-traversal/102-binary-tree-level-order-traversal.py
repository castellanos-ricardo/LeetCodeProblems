# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        res =[]
        
        while(queue):
            level = []
            levelSize = len(queue)
            for i in range(levelSize):
                current = queue.pop(0)
                if current:
                    level.append(current.val)
                    queue.append(current.left)
                    queue.append(current.right)
                
            if level:
                res.append(level)
        return res
            
            
            
            