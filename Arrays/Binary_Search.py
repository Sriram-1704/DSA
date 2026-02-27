class Solution:
    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left += 1
            else:
                right -= 1
        return -1
nums = [2,3,4,5,6,10]
target = 10
obj = Solution()
print(obj.binary_search(nums, target))
