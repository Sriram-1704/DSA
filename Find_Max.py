class Solution:
    def findMax(self,nums):
        if len(nums) == 0:
            return None
        maximum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > maximum:
                maximum = nums[i]
        return maximum
nums = [4,2,9,1,0]
obj = Solution()
print(obj.findMax(nums))