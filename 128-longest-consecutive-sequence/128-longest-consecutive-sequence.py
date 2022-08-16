class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #convert list to set, set lookup time complexity is O(1)
        s = set(nums)
        longestSequence = 0
        
        for num in s:    
            if (num -1) not in s:
                length = 0
                while((num+length) in s):
                    length += 1
                longestSequence = max(longestSequence, length)
        
        return longestSequence