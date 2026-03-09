class Solution:
    def quadratic_roots(self, a, b, c):
        D = b*b - 4*a*c
        if D > 0:
            root1 = (-b + D**0.5) / (2*a)
            root2 = (-b - D**0.5) / (2*a)
            return root1, root2
        elif D == 0:
            root = -b / (2*a)
            return root, root
        else:
            real = -b / (2*a)
            imag = (abs(D)**0.5) / (2*a)
            return f"{real}+{imag}i", f"{real}-{imag}i"
obj = Solution()
print(obj.quadratic_roots(1, -3, 2))
