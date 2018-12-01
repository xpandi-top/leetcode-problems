class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
        	return nums.index(target)
        if target <= nums[0]:
        	return 0
        if target >=nums[-1]:
        	return len(nums)
        i=0
        while target>nums[i]:
        	i=i+1
        return i

nums=[1,2,3,4]
target=4
print(Solution().searchInsert(nums, traget))