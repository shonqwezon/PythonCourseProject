"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-substring-with-given-hash-value/description
"""


class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        powers = pow(power, k, modulo)

        left = 0
        hash = 0
        for i in range(len(s) - 1, -1, -1):
            val = ord(s[i]) - ord("a") + 1
            hash = (hash * power + val) % modulo
            if i + k < len(s):
                prev_val = ord(s[i + k]) - ord("a") + 1
                hash = (hash - prev_val * powers) % modulo
            if hash == hashValue:
                left = i

        return s[left : left + k]


if __name__ == "__main__":
    s = Solution()
    print(s.subStrHash("leetcode", 7, 20, 2, 0))
