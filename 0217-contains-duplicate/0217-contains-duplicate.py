class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sets=set(nums)
        if len(sets)!=len(nums):
            return True
        else:
            return False
        # for i in sets:
        #     if nums.count(i)>1:
        #         return True
        # return False
        # dict1={}
        # for i in nums:
        #     if i not in nums:
        #         dict1[i]=1
        #     dict1[i]+=1
        # for i in dict1:
        #     if dict1[i]>1:
        #         return True
        # return False
         