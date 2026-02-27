class Solution:
    def rank_array(self, nums):
        sorted_unique = sorted(set(nums))

        rank = {}
        for i, num in enumerate(sorted_unique):
            rank[num] = i + 1

        for i in range(len(nums)):
            nums[i] = rank[nums[i]]
        
        return nums
nums = [40,30,10,20]
obj = Solution()
print(obj.rank_array(nums))