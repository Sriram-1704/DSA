class Solution:
    def power_of_digit(self, x, n):
        if n < 0:
            x = 1 / x  
            n = -n  

        result = 1

        while n > 0:
            if n % 2 == 1:
                result = result * x
            
            x = x * x
            n = n // 2
        return result
x = 2
n = -5
obj = Solution()
print(obj.power_of_digit(x,n))