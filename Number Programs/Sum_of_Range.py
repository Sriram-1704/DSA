class Solution:
    def sum_of_range(self, left, right):
        n = right - left + 1
        return n * (left + right) // 2
left = 1
right = 5
obj = Solution()
print(obj.sum_of_range(left, right))