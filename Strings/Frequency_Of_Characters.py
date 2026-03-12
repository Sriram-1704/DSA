class Solution:
    def charFrequency(self, s):
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        return freq

s = "hello"
obj = Solution()
result = obj.charFrequency(s)

for key, value in result.items():
    print(key, ":", value)