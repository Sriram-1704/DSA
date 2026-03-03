# class Solution:
#     def fibonacci(self, n):
#         if n <= 0:
#             return []
        
#         if n == 1:
#             return [0]
        
#         result = [0, 1]
#         a,b = 0,1

#         for _ in range(2, n):
#             c = a + b
#             result.append(c)
#             a = b
#             b = c
#         return result
# n = 5
# obj = Solution()
# print(obj.fibonacci(n))


# Recursive code

class Solution:
    def fibonacci(self, n):
        if n <= 0:
            return 0
        
        if n == 1:
            return 1
        
        return self.fibonacci(n -1) + self.fibonacci(n -2)

n = 3
obj = Solution()
print(obj.fibonacci(n))
