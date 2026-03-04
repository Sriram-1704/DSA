class Solution:
    def isAutomorphic(self, n):
        
        square = n * n
        
        # Count digits
        temp = n
        digits = 0
        
        if n == 0:
            return True
        
        while temp > 0:
            digits += 1
            temp //= 10
        
        return square % (10 ** digits) == n
n = 6
obj = Solution()
print(obj.isAutomorphic(n))