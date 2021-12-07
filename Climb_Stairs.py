class Solution:
    def climbStairs(self, n: int) -> int:
        
        def find_factorial(x):
            lis = [0]*x
            lis[0], lis[1] = 0, 1
            for i in range(2, x-1):
                lis[i] = lis[i-1] + lis[i-2]
            return lis[i]
        return find_factorial(n+3)
