class Solution:
    def isPalindrome(self, x):
        string=""
        string=str(x)
        temp=reversed(list(string))
        if(list(temp)==list(string)):
            return True
        else:
            return False


solution=Solution()
print(solution.isPalindrome(101))