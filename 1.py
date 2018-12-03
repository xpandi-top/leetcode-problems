class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        for i_index,i in enumerate(nums[:l-1]):
            for j_index,j in enumerate(nums[i_index+1:l]):
                if i +j == target:
                    return [i_index,j_index+i_index+1]
        """
        l = len(nums)

        for i_index in range(l-1):
            for j_index in range(i_index+1,l) :
                if nums[i_index]+nums[j_index]==target:
                    return [i_index,j_index]
