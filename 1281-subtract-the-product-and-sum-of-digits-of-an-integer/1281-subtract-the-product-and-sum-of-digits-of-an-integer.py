class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        list1=list(str(n))
        pro=1
        count=0
        for i in list1:
            pro*=int(i)
            count+=int(i)
        res=int(pro)-int(count)
        return res