class Solution:
    def max_min_digit(self, n):
        n = abs(n)
        if n == 0:
            return 0, 0
        max_digit = 0
        min_digit = 9

        while n > 0:
            digit = n % 10

            if digit > max_digit:
                max_digit = digit
            
            if digit < min_digit:
                min_digit = digit
            
            n = n // 10
        
        return max_digit, min_digit
n = 15327
obj = Solution()
print(obj.max_min_digit(n))