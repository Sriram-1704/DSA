class Solution:
    def findSubstring(self, s, sub):
        n = len(s)
        m = len(sub)
        
        # Edge case
        if m > n:
            return -1
        
        # Loop through main string
        for i in range(n - m + 1):
            j = 0
            
            # Check substring match
            while j < m:
                if s[i + j] != sub[j]:
                    break
                j += 1
            
            # If full match found
            if j == m:
                return i
        
        return -1


s = "hello world"
sub = "world"

obj = Solution()
print(obj.findSubstring(s, sub))