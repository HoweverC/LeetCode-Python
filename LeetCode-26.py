class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        j = 0
        len_nums = len(nums)
        for i in range(len_nums):
            if(nums[j] != nums[i]):
                nums[j+1] = nums[i]
                j += 1
        return j+1