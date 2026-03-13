class Solution:

    def removeDuplicates(self, s):

        seen = set()
        result = ""

        for ch in s:
            if ch not in seen:
                seen.add(ch)
                result += ch

        return result

s = "programming"
obj = Solution()
print(obj.removeDuplicates(s))