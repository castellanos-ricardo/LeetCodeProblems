# How can you go from input to output for a couple of examples? One way would be to calculate n! and then count the number of zeros but as we learned factorial grows exponentially so the number can get extremely large and cause an overflow problem. With that being said the solution discovered in 201 was to find the number of 5's in the formula for instance 5! has one five so therefore there is one zero, 20! has (5 x 1)(5 x 2)(5 x 3)(5 x 4) = 4 zeroes

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        quotient = n
        
        while True:
            quotient = quotient//5
            count = count + quotient
            if quotient<5:
                break
        return count
            
        
        