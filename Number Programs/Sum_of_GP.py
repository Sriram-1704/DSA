class Solution:
    def sum_of_gp(self, a, r, n):
        if r == 1:
            return a * n
        return a * (r ** n - 1) / (r - 1)
a = 2
r = 2
n = 5
obj = Solution()
print(obj.sum_of_gp(a, r, n))

'''
class Solution:
    def sumOfGP(self, a: float, r: float, n: int) -> float:
        total = 0
        current = a
        
        for _ in range(n):
            total += current
            current *= r
        
        return total
'''