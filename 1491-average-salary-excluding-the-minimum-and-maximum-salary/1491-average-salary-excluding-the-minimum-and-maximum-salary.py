class Solution:
    def average(self, salary: List[int]) -> float:
        ans=0
        salary.sort()
        # print(salary)
        for i in range(1,(len(salary)-1)):
            # print(salary[i])
            ans=salary[i]+ans
            # print(ans)
        print(ans)
        avg=ans/((len(salary)-2))
        return avg