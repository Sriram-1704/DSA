class Solution:
    def sum_of_digits(self, n):

        n = abs(n)
        total = 0

        while n > 0:
            digit = n % 10
            total = total + digit
            n = n // 10
        return total
n = 345
obj= Solution()
print(obj.sum_of_digits(n))