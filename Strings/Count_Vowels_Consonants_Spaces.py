class Solution:
    def countCharacters(self, s):
        
        vowels = 0
        consonants = 0
        spaces = 0
        
        for ch in s:
            
            if ch.lower() in "aeiou":
                vowels += 1
                
            elif ch == " ":
                spaces += 1
                
            elif ch.isalpha():
                consonants += 1
        
        return vowels, consonants, spaces


# Input
s = "Hello World"

# Object creation
obj = Solution()

# Function call
v, c, sp = obj.countCharacters(s)

print("Vowels:", v)
print("Consonants:", c)
print("Spaces:", sp)