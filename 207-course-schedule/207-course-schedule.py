class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjancecyList = {i:[] for i in range(numCourses)}
        
        for prereq in prerequisites:
            c, p = prereq
            adjancecyList[c].append(p)
        print(adjancecyList)
        
        visited = set()
        
        def dfs(node):
            if node in visited:
                return False
            if adjancecyList[node] == []:
                return True
            
            visited.add(node)
            for neighbor in adjancecyList[node]:
                if not dfs(neighbor): 
                    return False
            
            visited.remove(node)
            adjancecyList[node] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
            
        
        