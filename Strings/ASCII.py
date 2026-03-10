class Solution:
    def findASCII(self, ch):
        ascii_value = ord(ch)
        return ascii_value

ch = 'A'
obj = Solution()
print(obj.findASCII(ch))


'''
class Solution:
    def findASCII(self, ch):

        ascii_chars = ""
        
        for i in range(128):
            ascii_chars += chr(i)

        for i in range(len(ascii_chars)):
            if ascii_chars[i] == ch:
                return i


# Input
ch = 'A'

# Object creation
obj = Solution()

# Function call
print(obj.findASCII(ch))
'''