class Solution:
    def reverse_num(self, n):
        if n < 0:
            sign = -1
        else:
            sign = 1
        n = abs(n)
        reversed_num = 0

        while n != 0:
            digit = n % 10
            reversed_num = reversed_num * 10 + digit
            n = n // 10
        
        reversed_num *= sign

        if reversed_num < -2 ** 31 or reversed_num > 2 ** 31 -1:
            return 0
        
        return reversed_num
n = 12555555555555555555
obj = Solution()
print(obj.reverse_num(n))