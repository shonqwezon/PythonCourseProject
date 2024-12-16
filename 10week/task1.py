"""
https://leetcode.com/problem-list/binary-tree/
URL: https://leetcode.com/problems/path-sum-ii/description/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum(self, root, targetSum: int) -> list[list[int]]:
        result = []

        def dfs(node, cur_path, cur_sum):
            if not node:
                return

            cur_path.append(node.val)
            cur_sum += node.val

            if not node.left and not node.right and cur_sum == targetSum:
                result.append(list(cur_path))
            else:
                dfs(node.left, cur_path, cur_sum)
                dfs(node.right, cur_path, cur_sum)

            cur_path.pop()

        dfs(root, [], 0)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.pathSum([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 2))
