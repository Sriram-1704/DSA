class Solution:
    def sum_of_n(self, n):
        total = 0
        for i in range(1, n + 1):
            total = total + i
        return total
        # return n * (n + 1) // 2
n = 5
obj = Solution()
print(obj.sum_of_n(n))