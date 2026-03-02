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
    
    def range_of_palindromes(self, low, high):
        result = []

        for num in range(low, high + 1):
            if self.palindrome(num):
                result.append(num)
        return result
    
low = 100
high = 150
obj = Solution()
print(obj.range_of_palindromes(low, high))