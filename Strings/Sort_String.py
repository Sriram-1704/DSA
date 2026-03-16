class Solution:

    def sortString(self, s):

        arr = list(s)
        n = len(arr)

        for i in range(n):
            for j in range(0, n-i-1):

                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        return "".join(arr)

s = "program"
obj = Solution()
print(obj.sortString(s))


'''
class Solution:

    def sortString(self, s):

        sorted_chars = sorted(s)

        result = "".join(sorted_chars)

        return result


# Input
s = "program"

# Object creation
obj = Solution()

# Function call
print(obj.sortString(s))
'''