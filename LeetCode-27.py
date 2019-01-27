class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        j = 0
        len_nums = len(nums)
        for i in range(len_nums):
            if (nums[i] != val):
                nums[j] = nums[i]
                j += 1
        return j