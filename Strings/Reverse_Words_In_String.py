class Solution:
    def reverseWords(self, s):
        words = []
        word = ""
        
        # Step 1: Extract words manually
        for ch in s:
            if ch != ' ':
                word += ch
            else:
                if word != "":
                    words.append(word)
                    word = ""
        
        # Add last word
        if word != "":
            words.append(word)
        
        # Step 2: Reverse words manually
        left = 0
        right = len(words) - 1
        
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        
        # Step 3: Join words
        result = ""
        for i in range(len(words)):
            result += words[i]
            if i != len(words) - 1:
                result += " "
        
        return result

s = "  hello   world  python  "
obj = Solution()
print(obj.reverseWords(s))