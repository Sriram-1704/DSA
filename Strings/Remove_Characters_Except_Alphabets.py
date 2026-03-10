class Solution:
    def removeNonAlphabets(self, s):

        result = ""

        for ch in s:
            if ch.isalpha():
                result += ch

        return result


s = "He11o W@rld!123"
obj = Solution()
print(obj.removeNonAlphabets(s))