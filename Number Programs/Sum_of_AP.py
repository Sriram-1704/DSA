class Solution:
    def sum_of_ap(self, a, d, n):
        total = 0
        current = a

        for _ in range(n):
            total += current
            current += d
        
        return total
    
    # Using AP Formula
        # return n * (2 * a + (n - 1) * d) // 2
n = 5  # No of Terms
a = 2  # First Term
d = 2  # Difference
obj = Solution()
print(obj.sum_of_ap(a, d, n))