class Solution:

    def removeChars(self, str1, str2):

        remove_set = set(str2)

        result = ""

        for ch in str1:
            if ch not in remove_set:
                result += ch

        return result

str1 = "computer"
str2 = "cat"
obj = Solution()
print(obj.removeChars(str1, str2))