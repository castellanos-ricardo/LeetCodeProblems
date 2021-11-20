class Solution:
    def myAtoi(self, s: str) -> int:
        #we are look for 0-9 inside string, and a set has constant look up time
        nums = set('0123456789')
        result = 0 
        i = 0
        neg = 1
        if(len(s)== result):
            return result
        #eleminate whitespaces
        while(i < len(s) and s[i] == ' '):
            i = i +1
        #determine sign
        if(i<len(s) and s[i] == '-'):
            neg = -1
            i = i +1
        elif(i<len(s) and s[i] == '+'):
            i = i +1
        #itterate through the string, check if string is empty?
        while i < len(s):
            if s[i] in nums:
                result = result * 10 + int(s[i])
                i = i + 1
            else:
                break
        result = result * neg
        if result > (2**31 -1):
            return 2**31 -1
        elif result < -2**31:
            return -2**31
        else:
            return result
        