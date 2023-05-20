class Solution:
    def calPoints(self, operations: List[str]) -> int:
        list1=[]
        for i in operations:
            if i=='+':
                a=list1[-2]+list1[-1]
                list1.append(int(a))
            elif i=='C':
                list1.pop()
            elif i=='D':
                x=list1[-1]*2
                list1.append(int(x))
            else:
                list1.append(int(i))
        return sum(list1)
        