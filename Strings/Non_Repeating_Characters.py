class Solution:

    def nonRepeating(self, s):

        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        result = []

        for ch in s:
            if freq[ch] == 1:
                result.append(ch)

        return result
    
s = "programming"
obj = Solution()
output = obj.nonRepeating(s)

for ch in output:
    print(ch)