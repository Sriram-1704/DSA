class Solution:

    def capitalizeFirstLast(self, s):

        words = s.split()

        result = ""

        for word in words:

            if len(word) == 1:
                result += word.upper() + " "

            else:
                new_word = word[0].upper() + word[1:-1] + word[-1].upper()
                result += new_word + " "

        return result.strip()

s = "hello world python"
obj = Solution()
print(obj.capitalizeFirstLast(s))