class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        print(nums)
        return len(nums)

nums = [3,2,2,3]
val = 3

Solution().removeElement(nums,val)