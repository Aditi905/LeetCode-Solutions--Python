class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]
        count=nums[0]
        for i in range(1,len(nums)):
            ans=max(nums[i],nums[i]+ans)
            count=max(ans,count)
        return count
