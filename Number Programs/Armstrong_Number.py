class Solution:
    def is_armstrong(self, n):
        original = n
        power = len(str(n))
        total = 0

        while n > 0:
            digit = n % 10
            total = total + digit ** power
            n = n // 10
        
        return total == original
n = 1634
obj = Solution()
print(obj.is_armstrong(n))