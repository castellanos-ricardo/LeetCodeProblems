class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        res1 = ''
        res2 = ''
        
        for c in s:
            if c == '#' and stack1:
                stack1.pop()
            elif c == '#':
                pass
            else:
                stack1.append(c)
                
        for c2 in t:
            if c2 == '#' and stack2:
                stack2.pop()
            elif c2 == '#':
                pass
            else:
                stack2.append(c2)
        
        res1 += ''.join(stack1)
        res2 += ''.join(stack2)
        
        if res1 == res2:
            return True 
        else:
            return False
            