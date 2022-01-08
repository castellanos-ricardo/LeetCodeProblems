class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = self.buildGraph(edges)
        visited = set()
        return self.hasPath(graph,start,end,visited)
    
    #turn double integer array into a adjacency list
    def buildGraph(self,edges):
        graph={}
        for edge in edges:
            a,b = edge
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)
        return graph
    
    #depth first search with a set to keep track of visited nodes
    def hasPath(self,graph,src,dst,visited):
        if src == dst:
            return True
        if src in visited:
            return False
        visited.add(src)
        
        for neighbor in graph[src]:
            if self.hasPath(graph,neighbor,dst,visited):
                return True
        return False
    
