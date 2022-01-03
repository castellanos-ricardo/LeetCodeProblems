class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        if numRows==0:
            return triangle
        
        triangle.append([1])
        for i in range(1,numRows):
            newRow = []
            previousRow = triangle[-1]
            newRow.append(1)
            for j in range (1,i):
                newRow.append(previousRow[j-1] + previousRow[j])
            newRow.append(1)
            triangle.append(newRow)
            
        return triangle
                
                
        
        