class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        if(len(arr)==1):
            return [-1]
        result = []
        result.append(-1)
        
        #slice arr
        arr.pop(0)
        
        print(arr)
        
        for element in reversed(arr):
            result.insert(0,max(element, result[0]))
        
        return result
        