class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
    
    def mergeSort(self,nums):
        if len(nums) < 2:
            return nums
        m = len(nums)//2
        left = self.mergeSort(nums[:m])
        right = self.mergeSort(nums[m:])
        
        return self.merge(left,right)

        
    def merge(self, left, right):
        temp = [0] * (len(left) + len(right))
        l = r = k = 0
        
        while l< len(left) and r<len(right):
            if left[l] < right[r]:
                temp[k] = left[l]
                k += 1
                l+=1
            else:
                temp[k] = right[r]
                k += 1
                r+=1
        
        while l< len(left):
            temp[k] = left[l]
            k += 1
            l+=1
            
        while r< len(right):
            temp[k] = right[r]
            k += 1
            r+=1
        
        return temp