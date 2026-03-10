class Solution:

    def sumNumbers(self, s):

        total_sum = 0
        current_number = 0

        for ch in s:

            if '0' <= ch <= '9':
                current_number = current_number * 10 + (ord(ch) - ord('0'))

            else:
                total_sum += current_number
                current_number = 0

        total_sum += current_number

        return total_sum

s = "ab12cd3"
obj = Solution()
print(obj.sumNumbers(s))