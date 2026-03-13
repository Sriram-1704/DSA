class Solution:

    def printDuplicates(self, s):

        freq = {}

        # Count frequencies
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # Print duplicates
        for ch in freq:
            if freq[ch] > 1:
                print(ch)


s = "programming"
obj = Solution()
obj.printDuplicates(s)