class Solution:
    def is_strong_number(self, n):

        original = n
        total = 0

        while n > 0:
            digit = n % 10
            fact = 1
            for i in range(1, digit + 1):
                fact = fact * i

            total = total + fact
            n = n // 10

        return total == original
n = 145
obj = Solution()
print(obj.is_strong_number(n))