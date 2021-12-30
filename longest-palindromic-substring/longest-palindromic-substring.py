class Solution:
    def longestPalindrome(self, s: str) -> str:        
        oddLength = self.odd(s)
        evenLength = self.even(s)
        
        if len(oddLength)>= len(evenLength):
            return oddLength
        else:
            return evenLength

    def odd(self,s):
        longest_substring= ''
        
        for i in range(len(s)):
            l, r = i, i
            while l>=0 and r < len(s) and s[l]==s[r]:
                if (r-l +1) > len(longest_substring):
                    longest_substring = s[l:r+1]
                l-=1
                r+=1
        return longest_substring
                
    def even(self,s):
        longest_substring= ''
        
        for i in range(len(s)):
            l, r = i, i+1
            while l>=0 and r < len(s) and s[l]==s[r]:
                if (r-l +1) > len(longest_substring):
                    longest_substring = s[l:r+1]
                l -=1
                r +=1
        return longest_substring
                

        