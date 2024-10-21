"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/set-matrix-zeroes
"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:

        zer_col = set()
        zer_row = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not matrix[i][j]:
                    zer_col.add(j)
                    zer_row.add(i)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zer_row or j in zer_col:
                    matrix[i][j] = 0


if __name__ == "__main__":
    s = Solution()
    print(s.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
