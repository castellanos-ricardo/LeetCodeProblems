class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slowIterator = 0
        
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i], nums[slowIterator] = nums[slowIterator],nums[i]
                slowIterator += 1
        