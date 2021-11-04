#Time complexity: O(nlogn)  space complexity: O(1) 
    #solution - sort array then use a for loop index to check which is missing
    
#Time complexity: O(n)  space complexity: O(n) 
    #solution - create a list of array size to represent true or false if seen in given array
    
#Time complexity: O(n)  space complexity: O(1) 
    #solution - use sum of natural numbers formula and find the difference

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumOfSequence = (n*(n+1))//2
        
        return sumOfSequence - sum(nums)