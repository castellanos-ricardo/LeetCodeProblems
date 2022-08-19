class Solution:
    def isHappy(self, n: int) -> bool:
        #solution to problem is to check if we calculate the same number twice
        #therefore we can use a set
        s = set()
        
        while n not in s:
            result = 0
            s.add(n)
            n = self.sumOfSquares(n)
            
            if n ==1:
                return True
        return False
    
    def sumOfSquares(self,n):
        result = 0
        while n:
            #extract first number
            d = n%10
            #square digit and add to result
            result += d*d
            #remove first number
            n = n//10
        return result