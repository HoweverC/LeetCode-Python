class Solution:
    def fib(self, N: int) -> int:
        array = [i for i in range(N + 1)]
        for i in range(2,N + 1):
            array[i] = a[i - 1] + array[i - 2]
        return array[-1]