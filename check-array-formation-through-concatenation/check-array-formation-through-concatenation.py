class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        ps ={}
        for p in pieces:
            ps[p[0]] = p
        
        i= 0
        while i< len(arr):
            if arr[i] in ps:
                for pi in ps[arr[i]]:
                    if pi != arr[i]:
                        return False
                    i=i+1         
            else:
                return False
        return True
            

                            
                    

                    
            