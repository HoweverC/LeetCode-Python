class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        i = 5
        while n >= i:
            result += n // i
            i *= 5
        return result