class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m=m-1
        n=n-1
        while m+n+1>-1:
            if m<0 or(n>-1 and nums1[m]<nums2[n]):
                nums1[m+n+1]=nums2[n]
                n-=1
            else:
                nums1[m+n+1]=nums1[m]
                m-=1
        return nums1
        