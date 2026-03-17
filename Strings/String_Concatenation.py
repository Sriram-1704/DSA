class Solution:
    def concatenate(self, s1, s2):
        result = ""
        
        # Add characters of first string
        for ch in s1:
            result += ch
        
        # Add characters of second string
        for ch in s2:
            result += ch
        
        return result



s1 = "Hello"
s2 = "World"
obj = Solution()
print(obj.concatenate(s1, s2))