"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/unique-binary-search-trees/description/
"""


class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for node in range(2, n + 1):
            for root in range(1, node + 1):
                leftTree = dp[root - 1]
                rightTree = dp[node - root]
                dp[node] += leftTree * rightTree

        return dp[n]


if __name__ == "__main__":
    s = Solution()
    print(s.numTrees(3))
