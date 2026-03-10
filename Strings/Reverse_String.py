class Solution:
    def reverseString(self, s):

        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)

s = "hello"
obj = Solution()
print(obj.reverseString(s))

'''
class Solution:
    def reverseString(self, s):

        result = ""

        for i in range(len(s) - 1, -1, -1):
            result += s[i]

        return result

s = "hello"
obj = Solution()
print(obj.reverseString(s))
'''