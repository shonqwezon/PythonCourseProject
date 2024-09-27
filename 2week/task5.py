"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/text-justification
"""

from math import ceil
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        arr = [len(i) for i in words]
        res = []
        i = 0

        while i < len(arr):
            width = arr[i]
            res.append(words[i])
            j = i + 1
            while j < len(arr) and width + arr[j] + 1 <= maxWidth:
                width += arr[j] + 1
                j += 1
            wordCount = j - i
            diff = maxWidth - width
            if wordCount == 1:
                res[-1] += " " * diff
            if j < len(arr):
                for k in range(i + 1, j):
                    spaces = ceil(diff / (wordCount - 1))
                    diff -= spaces
                    res[-1] += " " * (spaces + 1) + words[k]
                    wordCount -= 1
            else:
                for k in range(i + 1, j):
                    res[-1] += " " + words[k]
            i = j
        res[-1] += " " * (maxWidth - len(res[-1]))
        return res


if __name__ == "__main__":
    s = Solution()
    print(
        s.fullJustify(
            [
                "Science",
                "is",
                "what",
                "we",
                "understand",
                "well",
                "enough",
                "to",
                "explain",
                "to",
                "a",
                "computer.",
                "Art",
                "is",
                "everything",
                "else",
                "we",
                "do",
            ],
            20,
        )
    )
