class Solution:

    
    def repeatedSubstringPattern(self, s: str) -> bool:
            
        def checkPattern(p,i):
	        #we are checking if p exists in s till the end
	        for sub in range(i,len(s),len(p)):
	            if(p != s[sub:sub+len(p)]):
	                return False
	        return True
        
        #edge case
        if(len(s)<=1):
            return False
        
        for i in range(1,(len(s)//2)+1):
            substring = s[:i]
            if(checkPattern(substring,i)):
                return True
    
        return False
                    
                