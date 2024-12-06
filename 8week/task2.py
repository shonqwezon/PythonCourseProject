"""
leetcode.com/problem-list/sliding-w/
url: https://leetcode.com/problems/count-zero-request-servers/description
"""


class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        intervals = []
        for i in sorted([(q - x, q, j) for j, q in enumerate(queries)]):
            intervals.append(i)
        res = [n] * len(queries)
        logs.sort(key=lambda x: x[1])
        logs.append([0, 10e6 + 1])
        left = right = 0
        w = {}

        for start, end, i in intervals:
            while logs[right][1] <= end:
                w[logs[right][0]] = w.get(logs[right][0], 0) + 1
                right += 1
            while logs[left][1] < start:
                w[logs[left][0]] -= 1
                if not w[logs[left][0]]:
                    del w[logs[left][0]]
                left += 1
            res[i] -= len(w)

        return res


if __name__ == "__main__":
    s = Solution()
    print(
        s.countServers(
            3,
            [[1, 35], [1, 32], [1, 11], [1, 39], [2, 29]],
            8,
            [38, 30, 23, 33, 15, 31, 34, 22, 11, 14],
        )
    )
