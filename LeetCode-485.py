class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        index = -1
        N = len(nums)
        result = 0
        for i, n in enumerate(nums):
            if n == 0:
                index = i
            else:
                result = max(result, i - index)
        return result