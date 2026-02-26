class Solution:
    def sortby_Freq(self, nums):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        nums.sort(key = lambda x : (-freq[x], x))

        return nums
nums = [4, 5, 6, 5, 4, 3]
obj = Solution()
print(obj.sortby_Freq(nums))