class Solution:
    def changeCase(self, s):
        result = ""
        
        for ch in s:
            # Check if lowercase
            if 'a' <= ch <= 'z':
                result += chr(ord(ch) - 32)
            
            # Check if uppercase
            elif 'A' <= ch <= 'Z':
                result += chr(ord(ch) + 32)
            
            else:
                # Keep other characters same
                result += ch
        
        return result


s = "Hello World!"
obj = Solution()
print(obj.changeCase(s))