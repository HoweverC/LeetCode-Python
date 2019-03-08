class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            s = 0
            while num >= 1:
                s += num % 10
                num //= 10
            num = s
        return num