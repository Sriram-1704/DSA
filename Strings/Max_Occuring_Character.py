class Solution:

    def maxOccurringChar(self, s):

        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        max_char = ""
        max_count = 0

        for ch in s:
            if freq[ch] > max_count:
                max_count = freq[ch]
                max_char = ch

        return max_char

s = "success"
obj = Solution()
print(obj.maxOccurringChar(s))