"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/unique-binary-search-trees-ii/description
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def func(self, start, end):
        if start > end:
            return [None]

        trees = []
        for i in range(start, end + 1):
            left_trees = self.func(start, i - 1)
            right_trees = self.func(i + 1, end)

            for left in left_trees:
                for right in right_trees:
                    trees.append(TreeNode(i, left, right))

        return trees

    def generateTrees(self, n: int):
        return self.func(1, n) if n else []


if __name__ == "__main__":
    s = Solution()
    print(s.generateTrees(3))
