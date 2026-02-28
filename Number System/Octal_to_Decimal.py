class Solution:
    def oct_to_dec(self, octal):
        decimal = 0
        for digit in octal:
            decimal = decimal * 8 + int(digit)
        return decimal
octal = "157"
obj = Solution()
print(obj.oct_to_dec(octal)) 