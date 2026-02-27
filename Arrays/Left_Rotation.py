class Solution:
    def left_rotation(self, nums, k):
        n = len(nums)
        k = k % n

        def reverseArray(self, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        reverseArray(self, 0 ,k-1)   # Reverse first k elements
        reverseArray(self, k, n-1)   # Reverse remaining elements
        reverseArray(self, 0, n-1)   # Reverse entire array
        return nums
nums = [1,2,3,4,5,6,7]
k = 3
obj = Solution()
print(obj.left_rotation(nums, k))