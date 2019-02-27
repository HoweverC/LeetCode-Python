class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return self.isIncrease(A) or self.isDecrease(A)

    def isIncrease(self,A):
        return all(A[i] - A[i+1] >= 0 for i in range(len(A) - 1))

    def isDecrease(self, A):
        return all(A[i] - A[i + 1] <= 0 for i in range(len(A) - 1))