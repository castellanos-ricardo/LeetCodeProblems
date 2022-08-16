class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        
        for index,num in list(enumerate(nums)):
            print(index,num)
            find = target -num
            if(find in dic):
                return [dic[find],index]
            dic[num] = index
                