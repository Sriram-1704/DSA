class Solution:
    def linear_search(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
nums = [1,2,3,4,5]
target = 3
obj = Solution()
print(obj.linear_search(nums, target))