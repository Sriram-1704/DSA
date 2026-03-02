class Solution:
    def is_perfect(self, n):
        if n < 1:
            return False
        
        total = 1

        i = 2
        while i * i <= n:    
            if n % i == 0:
                total = total + i
                if i != n // i:
                    total = total + n // i
            i = i + 1
        return total == n
n = 6
obj = Solution()
print(obj.is_perfect(n))