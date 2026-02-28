class Solution:
    def max_subarray_product(self, nums):
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            current = nums[i]
            if current < 0:
                max_product, min_product = min_product, max_product
            max_product = max(current, current*max_product)
            min_product = min(current, current*min_product)
            result = max(result, max_product)
        return result
nums = [2,3,-2,4]
obj = Solution()
print(obj.max_subarray_product(nums))
        