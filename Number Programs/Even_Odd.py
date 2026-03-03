class Solution:
    def even_odd(self, n):
        if (n & 1) == 0:
            return "Even"
        return "Odd"
    # def even_odd(self, n):
    #     if n % 2 == 0:
    #         return 'Even'
    #     return 'Odd'
n = 8
obj = Solution()
print(obj.even_odd(n))