class Solution:
    def factorial(self, n):
        if n < 0:
            return -1
        result = 1

        for i in range(1, n + 1):
            result = result * i

        return result
n = 5
obj = Solution()
print(obj.factorial(n))


'''
class Solution:
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)
'''