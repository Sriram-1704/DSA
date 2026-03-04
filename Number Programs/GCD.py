class Solution:
    def gcd(self, a, b):
        a = abs(a)
        b = abs(b)

        while b != 0:
            a , b = b , a % b
        return a
a = 48
b = 18
obj = Solution()
print(obj.gcd(a, b))