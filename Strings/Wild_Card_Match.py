class Solution:

    def isMatch(self, text, pattern):

        n = len(text)
        m = len(pattern)

        dp = [[False]*(n+1) for _ in range(m+1)]

        dp[0][0] = True

        # Handle patterns starting with *
        for i in range(1, m+1):
            if pattern[i-1] == '*':
                dp[i][0] = dp[i-1][0]

        for i in range(1, m+1):
            for j in range(1, n+1):

                if pattern[i-1] == text[j-1] or pattern[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]

                elif pattern[i-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

                else:
                    dp[i][j] = False

        return dp[m][n]


text = "baaabab"
pattern = "ba*a?"
obj = Solution()
print(obj.isMatch(text, pattern))