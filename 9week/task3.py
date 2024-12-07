"""
leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/unique-binary-search-trees/description/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]):
        ind = {v: i for i, v in enumerate(inorder)}

        def func(left, right):
            if left > right:
                return None

            root = TreeNode(postorder.pop())

            idx = ind[root.val]
            root.right = func(idx + 1, right)
            root.left = func(left, idx - 1)
            return root

        return func(0, len(inorder) - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))
