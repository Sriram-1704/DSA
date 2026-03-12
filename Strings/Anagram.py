class Solution:

    def isAnagram(self, s1, s2):

        if len(s1) != len(s2):
            return False

        freq = {}

        # Count characters of first string
        for ch in s1:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # Subtract using second string
        for ch in s2:
            if ch not in freq:
                return False
            else:
                freq[ch] -= 1

        # Check if all counts are zero
        for value in freq.values():
            if value != 0:
                return False

        return True

s1 = "listen"
s2 = "silent"
obj = Solution()
print(obj.isAnagram(s1, s2))