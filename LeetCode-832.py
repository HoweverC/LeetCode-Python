class Solution:
    def flipAndInvertImage(self, A: 'List[List[int]]') -> 'List[List[int]]':
        A = [row[::-1] for row in A]
        A = [list(map(lambda x: x ^ 1, row)) for row in A]
        return A