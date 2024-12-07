"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/print-binary-tree/description/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root):
        h = self.height(root)
        cols = 2 ** (h + 1) - 1
        mat = [[""] * cols for _ in range(h + 1)]
        if not root:
            return mat

        nodes = [(root, 0, cols // 2)]
        while nodes:
            node, r, c = nodes.pop()
            mat[r][c] = str(node.val)
            if node.left:
                nodes.append((node.left, r + 1, c - (2 ** (h - r - 1))))
            if node.right:
                nodes.append((node.right, r + 1, c + (2 ** (h - r - 1))))
        return mat

    def height(self, root) -> int:
        mx = 0
        nodes = [(root, 0)]
        while nodes:
            node, h = nodes.pop()
            if not node:
                continue
            mx = max(mx, h)
            nodes.append((node.left, h + 1))
            nodes.append((node.right, h + 1))
        return mx


if __name__ == "__main__":
    s = Solution()
    print(s.printTree([1, 2]))
