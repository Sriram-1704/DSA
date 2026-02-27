class Solution:
    def symmetric_pair(self, nums):
        seen = set()
        result = []

        for a,b in nums:
            if (b,a) in seen:
                result.append((b,a))
            else:
                seen.add((a,b))
        return result
nums = [(1,2), (3,4), (2,1), (5,6), (6,5)]
obj = Solution()
print(obj.symmetric_pair(nums))