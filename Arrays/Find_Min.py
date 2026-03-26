class Solution:
    def findMin(self,nums):
        if len(nums) == 0:
            return None
        minimum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < minimum:
                minimum = nums[i]
        return minimum
nums = [4,2,9,1,0]
obj = Solution()
print(obj.findMin(nums))

