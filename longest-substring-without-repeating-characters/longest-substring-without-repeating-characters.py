class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ''
        leftPointer = 0
        res = 0
    
        for i in range(len(s)):
            while s[i] in sub:
                sub = sub[1:]
                leftPointer = leftPointer + 1
            sub = sub + s[i]
            res = max(res, (i-leftPointer+1))
        return res
        