class Solution:
    def permutations(self, N, R):
        if R > N:
            return 0
        
        result = 1
        for i in range(R):
            result = result * (N - i)
        return result
N = 5
R = 3
obj = Solution()
print(obj.permutations(N, R))