class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=(n*(n + 1))//2
        print(total)
        ans=sum(nums)
        return total-ans

        # le = len(nums)
        # su = (le * (le + 1)) // 2
        # li_sum = sum(nums)
        # return su - li_sum