class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        result = [intervals[0]]
        
        for interval in intervals[1:]:
            start1, end1 = result[-1]
            start2, end2 = interval
            
            if start2 <= end1:
                result[-1][1] = max(end1, end2)
            else:
                result.append([start2, end2])
        return result
            
        
        