class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase=True
        decrease=True
        for i in range(len(nums)-1):
            increase=increase and nums[i+1] >= nums[i]
            decrease=decrease and nums[i+1] <= nums[i]
        return increase or decrease
        