class Solution:
    def sort_array(self, arr1, arr2):
        freq = {}

        for num in arr1:
            freq[num] = freq.get(num, 0) + 1
        
        result = []

        for num in arr2:
            if num in freq:
                result.extend([num] * freq[num])
                del freq[num]

        remaining = []

        for key in freq:
            remaining.extend([key] * freq[key])
        
        remaining.sort()

        return result + remaining
arr1 = [2,1,2,5,7,1,9,3,6,8,8]
arr2 = [2,1,8,3]
obj = Solution()
print(obj.sort_array(arr1, arr2))