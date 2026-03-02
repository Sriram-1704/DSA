class Solution:
    def palindrome(self, n):
        if n < 0 or (n % 10 == 0 and n != 0):
            return False
        
        reversed_half = 0

        while n > reversed_half:
            digit = n % 10
            reversed_half = reversed_half * 10 + digit
            n = n // 10
        
        return n == reversed_half or n == reversed_half // 10
n = 120
obj = Solution()
print(obj.palindrome(n))
