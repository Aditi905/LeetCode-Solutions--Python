class Solution:
    def hammingWeight(self, n: int) -> int:
      N=list(bin(n))
      count=0
      for i in range(len(N)):
        if N[i]=="1":
          count+=1
      return count
        