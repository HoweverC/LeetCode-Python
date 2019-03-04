class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        N = len(s)
        result = ""
        postion = 0
        while postion < N:
            temp = s[postion : postion + k]
            result = result + temp[::-1] + s[postion + k : postion + 2 * k]
            postion += 2 * k
        return result