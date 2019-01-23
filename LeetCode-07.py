class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x < 0):
            result = -1 * int(str(-x)[::-1])
        else:
            result = int(str(x)[::-1])
        if result > 2**31 or result < -1 * 2**31:
            result = 0
        return result