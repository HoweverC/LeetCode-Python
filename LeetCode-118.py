class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(0,numRows):
            result.append([1])
            for j in range(1,i+1):
                if j == i:
                    result[i].append(1)
                else:
                    result[i].append(result[i-1][j] + result[i-1][j-1])
        return  result