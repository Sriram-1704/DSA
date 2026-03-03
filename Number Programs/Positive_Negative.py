class Solution:
    def positive_negative(self, n):
        if n > 0:
            return "Positive"
        elif n < 0:
            return "Negative"
        else:
            return "Zero"
n = 19
obj = Solution()
print(obj.positive_negative(n))