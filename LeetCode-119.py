class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        for i in range(0,rowIndex+1):
            result.append([1])
            for j in range(1,i+1):
                if j == i:
                    result[i].append(1)
                else:
                    result[i].append(result[i-1][j] + result[i-1][j-1])
        return  result[rowIndex]