class Solution:
    def binary_to_decimal(self, binary):
        decimal = 0
        for digit in binary:
            decimal = decimal * 2 + int(digit)
        return decimal
binary = "1011"
obj = Solution()
print(obj.binary_to_decimal(binary)) 