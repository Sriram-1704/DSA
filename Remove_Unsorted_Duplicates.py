class Solution:
    def remove_duplicates(self,nums):
        seen = set()
        i = 0
    
        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[i] = num
                i += 1
    
        return i , nums # number of unique elements
    # def removeDuplicates(self, nums):
    #     seen = set()
    #     result = []
        
    #     for num in nums:
    #         if num not in seen:
    #             seen.add(num)
    #             result.append(num)
    #     return result
nums = [4,5,1,5,6,1,4,9]
obj = Solution()
print(obj.remove_duplicates(nums))