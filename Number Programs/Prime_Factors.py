class Solution:
    def prime_factors(self, n):
        factors = []

        while n % 2 == 0:
            factors.append(2)
            n = n // 2
        
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n = n // i
            i = i + 2
        
        if n > 2:
            factors.append(n)
        
        return factors
n = 60
obj = Solution()
print(obj.prime_factors(n))
        
