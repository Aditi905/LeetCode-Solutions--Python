class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        perimeter=0
        n=len(nums)
        nums.sort(reverse = True)
 
        for i in range(0, n - 2):
            if nums[i] < (nums[i + 1] + nums[i + 2]):
                perimeter = max(perimeter, nums[i] + nums[i + 1] + nums[i + 2])
        if perimeter==0:
            return 0
        else:
            return perimeter
                    
        
        