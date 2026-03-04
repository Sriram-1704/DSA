class Solution:
    def harshad_number(self, n):
         original = n
         total = 0

         while n > 0:
              digit = n % 10
              total = total + digit
              n = n // 10
            
         return original % total == 0   # 18 % 9 == 0
n = 18
obj = Solution()
print(obj.harshad_number(n))