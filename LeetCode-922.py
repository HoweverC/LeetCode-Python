class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = [x for x in A if x % 2 == 1]
        even = [x for x in A if x % 2 == 0]
        result = []
        judge = True
        while odd or even:
            if judge:
                result.append(even.pop())
            else:
                result.append(odd.pop())
            judge = not judge
        return result
