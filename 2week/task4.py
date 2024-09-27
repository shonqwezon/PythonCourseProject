"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/wildcard-matching/
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(p)
        m = len(s)
        dp = [[0] * (m + 1) for i in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            if p[i - 1] == "*":
                dp[i][0] = dp[i - 1][0]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[i - 1] == "*":
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[i - 1] == s[j - 1] or p[i - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[n][m]


if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("cbaala", "*a?*a*"))
