# class Solution:
#     def subset_array(self, arr1, arr2):
#         s = set(arr1)

#         for num in arr2:
#             if num not in s:
#                 return False
#         return True
# arr1 = [1,2,2,3,4]
# arr2 = [2,4]
# obj = Solution()
# print(obj.subset_array(arr1, arr2))

class Solution:
    def subset_array(self, arr1, arr2):
        freq = {}

        for num in arr1:
            freq[num] = freq.get(num, 0) + 1
        
        for num in arr2:
            if num not in freq or freq[num] == 0:
                return False
            freq[num] -= 1
        return True
arr1 = [1,2,2,3,4]
arr2 = [2,4]
obj = Solution()
print(obj.subset_array(arr1, arr2))
