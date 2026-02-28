class Solution:
    def dec_to_bin(self, n):
        if n == 0:
            return "0"
        result = ""
        while n > 0:
            remainder = n % 8
            result = str(remainder) + result
            n = n // 8
        return result
n = 100
obj = Solution()
print(obj.dec_to_bin(n))