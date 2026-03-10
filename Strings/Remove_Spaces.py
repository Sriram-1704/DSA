class Solution:
    def removeSpaces(self, s):

        result = ""

        for ch in s:
            if ch != " ":
                result += ch

        return result

s = "Hello World Python"
obj = Solution()
print(obj.removeSpaces(s))