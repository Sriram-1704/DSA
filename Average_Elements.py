class Solution:
    def calculate_sum(self, nums):
        total = 0
        for num in nums:
            total = total + num
        return total/len(nums)
nums = [1,2,3,4,5]
obj = Solution()
print(obj.calculate_sum(nums))