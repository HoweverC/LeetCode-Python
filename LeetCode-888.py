class Solution:
    def fairCandySwap(self, A: 'List[int]', B: 'List[int]') -> 'List[int]':
        sum_A, sum_B, set_B = sum(A), sum(B), set(B)
        target = (sum_A + sum_B) / 2
        for a in A:
            b = target - (sum_A - a)
            if b >= 1 and b <= 100000 and b in set_B:
                return [a, b]