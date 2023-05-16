class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # pro=0
        # for i in range(1, (len(nums)-1)):
        #     ans=nums[i-1]*nums[i]*nums[i+1]
        #     if pro<abs(ans):
        #         pro=ans
        # return pro

        # list1=[]
        # for i in range(len(nums)-2):
        #     for j in range(i+1, (len(nums)-1)):
        #         for k in range(j+1,(len(nums))):
        #             list1.append(nums[i]*nums[j]*nums[k])
        # #print(list1)
        # return max(list1)

        nums.sort()
        n=len(nums)
        max_pro=-10000000000000
        max_pro = max(max_pro, nums[0]*nums[1]*nums[n-1])
        max_pro = max(max_pro, nums[n-3]*nums[n-2]*nums[n-1])
        return max_pro
        