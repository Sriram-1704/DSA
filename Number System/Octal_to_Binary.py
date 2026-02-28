class Solution:
    def oct_to_bin(self, octal):
        lookup = {'0':'000','1':'001','2':'010','3':'011',
                  '4':'100', '5': '101', '6': '110', '7': '111'
                  }
        result = ""

        for digit in octal:
            result = result + lookup[digit]
        
        return result.lstrip("0") or "0"
octal = "157"
obj = Solution()
print(obj.oct_to_bin(octal))