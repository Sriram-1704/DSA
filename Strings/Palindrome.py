class Solution:
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True


s = "madam"
obj = Solution()
print(obj.isPalindrome(s))

'''
class Solution:
    def isPalindrome(self, s):
        
        cleaned = ""

        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        left = 0
        right = len(cleaned) - 1

        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1

        return True


s = "A man, a plan, a canal: Panama"
obj = Solution()
print(obj.isPalindrome(s))
'''