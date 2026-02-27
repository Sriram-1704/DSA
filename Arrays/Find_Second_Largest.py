class Solution:
    def secondLargest(self,nums):
        if len(nums) < 2:
            return -1
        largest = second_largest = float('-inf')  # float('-inf') is smaller than every real number
        for num in nums:
            if num > largest:
                second_largest = largest
                largest = num
            elif num < largest and num > second_largest:
                second_largest = num
        if second_largest == float('-inf'):
            return -1
        return second_largest
nums = [4,2,9,1,7]
obj = Solution()
print(obj.secondLargest(nums))