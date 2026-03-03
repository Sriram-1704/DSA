class Solution:
    def max_of_num(self, a , b):
        if a > b:
            return a
        else:
            return b
a = 10
b = 20
obj = Solution()
print(obj.max_of_num(a, b))