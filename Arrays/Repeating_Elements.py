class Solution:
    def repeat_elements(self, nums):
        freq = {}
        result = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key in freq:
            if freq[key] > 1:
                result.append(key)
        
        return result
nums = [1,2,3,4,5,2,3]
obj = Solution()
print(obj.repeat_elements(nums))
