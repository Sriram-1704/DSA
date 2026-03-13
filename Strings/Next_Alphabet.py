class Solution:

    def nextAlphabet(self, s):

        result = ""

        for ch in s:

            if ch == 'z':
                result += 'a'

            elif ch == 'Z':
                result += 'A'

            else:
                result += chr(ord(ch) + 1)

        return result


s = "abcdz"
obj = Solution()
print(obj.nextAlphabet(s))