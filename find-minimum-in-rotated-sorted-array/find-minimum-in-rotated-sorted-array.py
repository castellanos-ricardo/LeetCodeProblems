class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        begin=0
        end = len(nums) -1
        
        while(begin <= end):
            if(nums[begin]<nums[end]):
                res = min(nums[begin],res)
                break
                
            middle = (begin + end) //2  
            res = min(res, nums[middle])
            
            if(nums[begin]>nums[middle]):
                end = middle -1
            else:
                begin = middle + 1

        return res
                
            
            
        