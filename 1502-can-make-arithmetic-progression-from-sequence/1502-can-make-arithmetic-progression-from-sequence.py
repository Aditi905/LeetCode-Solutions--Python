class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        ans=arr[0]-arr[1]
        for i in range(1,len(arr)-1):
            if (arr[i]-arr[i+1])!=ans:
                return False
        else:
            return True
        
        # arr = sorted(arr)
        # diff = arr[0] - arr[1]
        # for i in range(1,len(arr)-1):
        #     if arr[i]-arr[i+1] != diff:
        #         return False
        # return True