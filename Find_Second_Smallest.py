class Solution:
    def secondSmallest(self, nums):
        if len(nums) < 2:
            return -1
        smallest = second_smallest = float('inf')  # float('inf') is greater than every real number
        for num in nums:
            if num < smallest:
                second_smallest = smallest
                smallest = num
            elif num > smallest and num < second_smallest:
                second_smallest = num
        if second_smallest == float('inf'):
            return -1
        return second_smallest
nums = [4,2,2,9,1,7]
obj = Solution()
print(obj.secondSmallest(nums))