class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
    
        if len(nums) == 0:
            return output
        if len(nums)== 1:
            return [nums]
        
        for i in range(len(nums)):
            element = nums[i]
            rest = nums[0:i] + nums[i+1:]
        
            for p in self.permute(rest):
                output.append([element] + p)
    
        return output
        