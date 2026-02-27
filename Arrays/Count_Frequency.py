class Solution:
    def count_frequency(self, nums):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        return freq
nums = [1,2,2,3,1,4,1]   
obj = Solution()
print(obj.count_frequency(nums))

