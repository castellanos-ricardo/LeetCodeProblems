class Solution:
    def mySqrt(self, x: int) -> int:
        if x <2:
            return x
        
        l = 1
        r = x
        while(l<=r):
            mid = (l+r) //2             
            if (math.trunc(mid*mid) == x):
                return mid
            elif (math.trunc(mid*mid) > x):
                r = mid -1
            else:
                l = mid +1
        return l-1
                
                
                
            
        