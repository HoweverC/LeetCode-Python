class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                print(nums[i])
                print(nums[j])
                if (nums[i] + nums[j] == target):
                    return i,j

nums=[3,2,3]
target=6
solution=Solution()
print(solution.twoSum(nums,target))