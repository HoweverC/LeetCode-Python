class Solution:
    def romanToInt(self, s):
        num = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        sum = 0
        max = 1
        for i in xrange(len(s)-1,-1,-1):
            if num[s[i]] >= max:
                max = num[s[i]]
                sum += num[s[i]]
            else:
                sum -= num[s[i]]
        return  sum