class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res=len(list1)+len(list2)
        dict1={}
        for i in range(len(list1)):
            if list1[i] in list2:
                j=list2.index(list1[i])
                c=i+j
                res=min(res,c) 
                if list1[i] not in dict1:
                    dict1[list1[i]]=c
        l=[]
        for x,y in dict1.items():
            if y==res:
                l.append(x)
        return l
