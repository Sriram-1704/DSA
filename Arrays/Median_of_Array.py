class Solution:
    def findMedian(self, nums):
        nums.sort()
        n = len(nums)
        if n % 2 == 1:
            return nums[n // 2]
        else:
            mid1 = nums[ n // 2 - 1]
            mid2 = nums[ n // 2]
            return (mid1 + mid2)/2
nums = [5,3,6,1,7,4]
obj = Solution()
print(obj.findMedian(nums))