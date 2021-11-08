class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #bottom row is initialize to ones
        row = [1] * n
        
        #for loop to stack (m-1) rows
        for roww in range(m-1):
            #intialize new row with ones since last element is always 1
            newRow = [1]*n
            #second loop to access the elements and add(+) right neioghbor and below neighbor
            for col in range(n-2,-1,-1):
                newRow[col] = newRow[col+1] + row[col]
            #bottom row is reassigned
            row = newRow
        #return first element of the last row created
        return row[0] 