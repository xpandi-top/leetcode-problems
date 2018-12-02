class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums2=nums2+nums1[:m]
        nums2.sort()
        nums1[:n+m]=nums2

        print(nums1)

nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3

Solution().merge(nums1,m,nums2,n)