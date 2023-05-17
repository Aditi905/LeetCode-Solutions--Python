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
        #for minimum mahattan distance
#         list1=[]
#         minimum=1000000
#         for i in points:
#             # print(i)
#             # print(i[0])
#             if(i[0]==x or i[1]==y):
#                 list1.append(i)
#         print(list1)
#         if len(list1)==0:
#             return -1
#         if len(list1)==1:
#             return 0
#         else:
#             for i in range(len(list1)):
#                 ans=0
#                 for j in range(i+1,len(list1)):
#                     ans = (abs(list1[i][0] - list1[j][0]) +abs(list1[i][1] - list1[j][1]))
#                     minimum=min(minimum,ans)
#         return minimum
    
    
    
