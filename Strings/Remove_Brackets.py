class Solution:
    def removeBrackets(self, expr):

        stack = [1]
        sign = 1
        result = ""

        i = 0

        while i < len(expr):

            if expr[i] == '+':
                sign = stack[-1]

            elif expr[i] == '-':
                sign = -stack[-1]

            elif expr[i] == '(':
                stack.append(sign)

            elif expr[i] == ')':
                stack.pop()

            else:
                if sign == 1:
                    result += '+' + expr[i]
                else:
                    result += '-' + expr[i]

            i += 1

        if result[0] == '+':
            result = result[1:]

        return result
    
expr = "a-(b+c)"
obj = Solution()
print(obj.removeBrackets(expr))