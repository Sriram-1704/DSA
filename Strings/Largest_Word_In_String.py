class Solution:

    def largestWord(self, s):

        max_word = ""
        current_word = ""

        for ch in s:

            if ch != ' ':
                current_word += ch
            else:
                if len(current_word) > len(max_word):
                    max_word = current_word
                current_word = ""

        # Check last word
        if len(current_word) > len(max_word):
            max_word = current_word

        return max_word

s = "Python is a powerful language"
obj = Solution()
print(obj.largestWord(s))