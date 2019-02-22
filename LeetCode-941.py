class Solution:
    def validMountainArray(self, A: 'List[int]') -> 'bool':
        if len(A) < 3:
            return False
        max_num = A.index(max(A))
        if (max_num == 0) or (max_num == len(A) - 1):
            return False
        for i in range(0,max_num):
            if (A[i+1] <=  A[i]):
                return False
        for i in range(max_num+1,len(A)):
            if A[i] >= A[i-1]:
                return False
        return True