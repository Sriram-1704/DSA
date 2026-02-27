class Solution:
    def right_rotation(self, nums, k):
        n = len(nums)
        k = k % n
        def reverseArray(self, left, right):
            while left< right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        reverseArray(self,0, n-1)    # Entire Array Rotation
        reverseArray(self,0, k-1)    # Upto k terms rotation
        reverseArray(self,k, n-1)    # kth term to last term Rotation
        return nums
nums = [1,2,3,4,5,6,7]
k = 3
obj = Solution()
print(obj.right_rotation(nums, k))
