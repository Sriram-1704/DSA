class Solution:
    def is_prime(self, n):
        if n <= 1:
            return False
        
        if n <= 3:
            return True
        
        if n % 2 == 0 or n % 3 == 0:
            return False
        
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            
            i += 6
        return True
    
    def range_of_primes(self, low, high):
        result = []

        for num in range(low, high+1):
            if self.is_prime(num):
                result.append(num)
        
        return result
low = 100
high = 150
obj = Solution()
print(obj.range_of_primes(low, high))