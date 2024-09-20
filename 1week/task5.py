"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/regular-expression-matching/
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(p)
        m = len(s)

        dp = [[0] * (n + 1) for i in range(m + 1)]
        dp[0][0] = 1

        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == s[i - 1] or p[j - 2] == ".":
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        return dp[m][n]


if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("aabbl", "c*a*b*.l"))
