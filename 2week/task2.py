"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/permutation-in-string
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l_s1, l_s2 = len(s1), len(s2)
        if l_s1 > l_s2:
            return False
        s1_set = set(s1)
        s1_hash = sum([ord(i) for i in s1])
        cur_hash = sum([ord(s2[i]) for i in range(l_s1)])
        first, last = 0, l_s1
        while last < l_s2:
            if s1_hash == cur_hash and s1_set == set(s2[first:last]):
                return True
            cur_hash -= ord(s2[first])
            first += 1
            cur_hash += ord(s2[last])
            last += 1
        return s1_hash == cur_hash and s1_set == set(s2[first:last])


if __name__ == "__main__":
    s = Solution()
    print(s.checkInclusion("ab", "eidbaooo"))
