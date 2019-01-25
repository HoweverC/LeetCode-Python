class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [None]
        dict = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in dict:
                if dict[i] != stack.pop():
                    return False
            else:
                stack.append(i)
        return len(stack) == 1
