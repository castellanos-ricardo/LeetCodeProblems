import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if(n <= 0):
            return False
        
        i=0
        x=0
        while (x <= (2**31-1)):
            x = 3**i
            if x == n:
                return True
            i = i+1
        
#         if(3**i%n == 0):
#             return True
        
        return False

            
        