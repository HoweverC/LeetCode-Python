class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        size = len(nums)
        if size % 2 ==0:
            return int((nums[size // 2] + nums[size // 2 - 1]) / 2)
        if size % 2 == 1:
            return int(nums[(size - 1) // 2])