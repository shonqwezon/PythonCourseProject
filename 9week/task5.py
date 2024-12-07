"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/maximum-width-of-binary-tree/description/
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root) -> int:
        q = deque([(root, 0)])
        mx_w = -1
        while q:
            si = q[0][1]
            for _ in range(len(q)):
                node, lev = q.popleft()
                if node.left:
                    q.append((node.left, 2 * lev + 1))
                if node.right:
                    q.append((node.right, 2 * lev + 2))
            mx_w = max(mx_w, lev - si + 1)
        return mx_w


if __name__ == "__main__":
    s = Solution()
    print(s.widthOfBinaryTree([1, 2]))
