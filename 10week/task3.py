"""
https://leetcode.com/problem-list/binary-tree/
URL: https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root) -> int:
        def dfs(node, cur):
            if not node:
                return 0

            cur = cur * 10 + node.val

            if not node.left and not node.right:
                return cur

            l_sum = dfs(node.left, cur)
            r_sum = dfs(node.right, cur)

            return l_sum + r_sum

        return dfs(root, 0)


if __name__ == "__main__":
    s = Solution()
    print(s.sumNumbers([1, 2, 3]))
