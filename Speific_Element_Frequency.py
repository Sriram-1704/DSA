class Solution:
    def specific_freq(self, nums, k):
        count = 0
        for num in nums:
            if num == k:
                count += 1
        return {k : count}
nums = [1,1,2,3,2,4,2]
k = 5
obj = Solution()
print(obj.specific_freq(nums, k))