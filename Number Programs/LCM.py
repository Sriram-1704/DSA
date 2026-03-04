class Solution:
    def lcm(self, a, b):

        if a == 0 or b == 0:
            return 0
        
        def gcd(x,y):
            while y != 0:
                x, y = y, x % y
            return x
        
        return abs(a * b) // gcd(a , b)
a = 4
b = 6
obj = Solution()
print(obj.lcm(a, b))
    