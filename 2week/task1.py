"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/string-to-integer-atoi
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        is_negative = False
        is_num = False
        for i in s:
            if i == " ":
                if is_num:
                    break
                continue
            if i == "-" or i == "+":
                if is_num:
                    break
                is_negative = i == "-"
                is_num = True
                continue
            if ord("0") <= ord(i) <= ord("9"):
                if not is_num:
                    is_num = True
                res *= 10
                add = ord(i) - ord("0")
                res += add
                if is_negative and res > 2**31:
                    res = 2**31
                    break
                elif not is_negative and res > 2**31 - 1:
                    res = 2**31 - 1
                    break
                continue

            # This is forbidden char → quit
            break
        return res * (-1 if is_negative else 1)


if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("42"))
