#Understand
    #Input: integer n
    #Output: count of all primes less than n
#Match
#list of true or false values, assume all true at first
#for loop to check each number up to n
    #for loop to filter out multiples

class Solution:
    def countPrimes(self, n: int) -> int:
        #Plan
        if n <= 2:
            return 0
        primes = [True] * n             #Space complexity: O(n)
        primes[0]=primes[1] = False
        
        for i in range(2,int(math.sqrt(n))+1):  #Time complexity: O(n**1.5)
            if(primes[i]):
                for j in range(i**2,n,i):
                    primes[j] = False
        return sum(primes)                      #O(n)
        
        

#Review
#Evaluate