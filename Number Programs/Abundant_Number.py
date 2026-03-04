class Solution:
    def abundant(self, n):

        if n <= 1:
            return False
        
        divisor_sum = 1

        i = 2
        while i * i <= n:
            if n % i == 0:
                divisor_sum = divisor_sum + i

                if i != n // i:
                    divisor_sum = divisor_sum + n // i
            
            i = i + 1
        
        return divisor_sum > n
n = 12
obj = Solution()
print(obj.abundant(n))