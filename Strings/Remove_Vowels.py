class Solution:
    def removeVowels(self, s):

        result = ""

        for ch in s:
            if ch.lower() not in "aeiou":
                result += ch

        return result

s = "Hello World"
obj = Solution()
print(obj.removeVowels(s))