class Solution:

    def countWords(self, s):

        word_count = 0
        n = len(s)

        for i in range(n):

            if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
                word_count += 1

        return word_count

s = "I love Python programming"
obj = Solution()
print(obj.countWords(s))


'''
class Solution:
    
    def countWords(self, s: str) -> int:
        
        count = 0
        in_word = False
        
        for ch in s:
            
            if ch != " " and in_word == False:
                count += 1
                in_word = True
                
            elif ch == " ":
                in_word = False
        
        return count
'''