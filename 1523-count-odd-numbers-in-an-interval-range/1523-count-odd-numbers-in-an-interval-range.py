class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # count=0
        # for i in range(low,high+1):
        #     if i%2:
        #         count+=1
        # return count
        n=(high - low) // 2
        print(n)
        if(low%2!=0 or high%2!=0):
            n+=1
        return n
        