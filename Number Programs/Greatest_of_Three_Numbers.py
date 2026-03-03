class Solution:
    def greatest_of_three(self, a, b, c):
        if a >= b and a >= c:
            return a
        elif b >= a and b >= c:
            return b
        else:
            return c
        
a = 4
b = 3
c = 7
obj = Solution()
print(obj.greatest_of_three(a,b,c))