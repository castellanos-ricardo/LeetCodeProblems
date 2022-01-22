class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        name = ''
        
        for c in path + '/':
            if c == '/':
                if name == '..' and stack:
                    stack.pop()
                elif name != '' and name != '.' and name!= '..':
                    stack.append(name)
                name = ''
            else:
                name += c
        
        return '/'+ '/'.join(stack)
        