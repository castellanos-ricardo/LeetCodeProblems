class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = {}
        
        for l in s:
            if l in letters:
                letters[l]= letters[l] + 1
            else:
                letters[l] = 1
        
        for key, value in letters.items():
            if(value == 1 ):
                return s.index(key)
        
        return -1
        