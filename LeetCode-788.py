class Solution:
    def rotatedDigits(self, N: 'int') -> 'int':
        """
        :type N: int
        :rtype: int
        """
        result = 0
        for num in range(1, N + 1):
            if any(x in str(num) for x in ["3", "4", "7"]):
                continue
            if any(x in str(num) for x in ["2", "5", "6", "9"]):
                result += 1
        return result