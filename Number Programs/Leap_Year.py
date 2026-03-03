class Solution:
    def isLeapYear(self, year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False
year = 2024
obj = Solution()
print(obj.isLeapYear(year))