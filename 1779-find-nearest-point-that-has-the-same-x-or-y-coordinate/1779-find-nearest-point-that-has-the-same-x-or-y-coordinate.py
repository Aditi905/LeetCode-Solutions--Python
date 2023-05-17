class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        minimum=1000000
        index=-1
     
        for i in range(len(points)):
            if (x == points[i][0] or y == points[i][1]):
                ans=abs(x - points[i][0]) + abs(y - points[i][1])
                if ans<minimum:
                    minimum=ans
                    index=i
                    
        return index
    
    
    
