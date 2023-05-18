class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s)==0:
            return t
        dict1={}
        for i in t:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        for i in s:
            if i in dict1:
                dict1[i]-=1
        for i in dict1:
            if dict1[i]!=0:
                return i
                        
            
        