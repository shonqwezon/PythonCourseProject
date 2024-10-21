"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""


class Solution:
    d = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def func(self, letters, next_num):
        res = []
        if not next_num:
            res.append(letters)
            return res

        for letter in self.d[next_num[0]]:
            res.extend(self.func(letters + letter, next_num[1:]))
        return res

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        return self.func("", digits)


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))
