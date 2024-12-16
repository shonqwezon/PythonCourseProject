"""
https://leetcode.com/problem-list/binary-tree/
URL: https://leetcode.com/problems/longest-univalue-path/description/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root) -> int:
        self.longest_path = 0

        def dfs(node) -> int:
            if not node:
                return 0

            l_len = dfs(node.left)
            r_len = dfs(node.right)

            l_arr = r_arr = 0
            if node.left and node.left.val == node.val:
                l_arr = l_len + 1
            if node.right and node.right.val == node.val:
                r_arr = r_len + 1

            self.longest_path = max(self.longest_path, l_arr + r_arr)

            return max(l_arr, r_arr)

        dfs(root)
        return self.longest_path


if __name__ == "__main__":
    s = Solution()
    print(s.longestUnivaluePath([5, 4, 5, 1, 1, None, 5]))
