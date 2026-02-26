class Solution:
    def sort_array(self, nums):
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        mid = (n + 1)// 2
        # first_half = nums[:mid]
        # second_half = nums[mid:]
        # second_half.reverse()
        # return first_half + second_half

        left , right = mid, n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums

nums = [4,6,2,1,7,8,9]
obj = Solution()
print(obj.sort_array(nums))