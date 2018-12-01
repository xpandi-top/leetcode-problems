class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        l=len(nums)
        while i<(l-1):
        	if nums[i+1]==nums[i]:
        		nums.remove(nums[i+1])
        		l=l-1
        	else:
        		i=i+1
        #print(nums)
        return len(nums)




a = [12,3,3,4,4]
print(Solution().removeDuplicates(a))



