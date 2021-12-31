class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetRow = None
        row = 0
        
        while row < len(matrix):
            if matrix[row][0]<=target<= matrix[row][len(matrix[row])-1]:
                targetRow = row
                break
            row += 1
        
        if targetRow == None:
            return False
        
        l,r = 0, len(matrix[targetRow]) -1
        
        while l<= r:
            m = (l+r) //2
            if target< matrix[targetRow][m]:
                r = m -1
            elif target> matrix[targetRow][m]:
                l = m +1
            else:
                return True
        return False
        
        
        