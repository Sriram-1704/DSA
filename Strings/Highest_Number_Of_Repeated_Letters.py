class Solution:
    def maxRepeatingWord(self, s):
        words = s.split()
        
        max_repeat = 1
        result = "-1"
        
        for word in words:
            freq = {}
            
            for ch in word:
                if ch in freq:
                    freq[ch] += 1
                else:
                    freq[ch] = 1
            

            current_max = max(freq.values())
            
            if current_max > max_repeat:
                max_repeat = current_max
                result = word
        
        return result


s = "hello apple banana orange"
obj = Solution()
print(obj.maxRepeatingWord(s))