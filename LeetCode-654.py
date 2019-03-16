class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        node = TreeNode(max(nums))
        i = nums.index(max(nums))
        if nums[:i]:
            node.left = self.constructMaximumBinaryTree(nums[:i])
        if nums[i+1:]:
            node.right = self.constructMaximumBinaryTree(nums[i+1:])
        return node