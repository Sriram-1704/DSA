class Solution:
    def isPrime(self, num):
        if num < 2:
            return False
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        
        return True
    
    
    def canBeSumOfTwoPrimes(self, n):
        
        for i in range(2, n):
            if self.isPrime(i) and self.isPrime(n - i):
                return True
        
        return False
num = 39
obj = Solution()
print(obj.canBeSumOfTwoPrimes(num))