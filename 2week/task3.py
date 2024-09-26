"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/validate-ip-address
"""


class Solution:
    IP4 = "IPv4"
    IP6 = "IPv6"
    NONE = "Neither"

    def isIP4(self, queryIP: str):
        for i, octet in enumerate(queryIP.split(".")):
            try:
                if len(octet) == 0 or octet[0].isspace():
                    return self.NONE
                if i == 0 and octet[0] == "0":
                    return self.NONE
                if len(octet) != 1 and octet[0] == "0":
                    return self.NONE
                num = int(octet)
                if num > 255 or num < 0:
                    return self.NONE
            except Exception:
                return self.NONE
        return self.IP4

    def isIP6(self, queryIP: str):
        for octet in queryIP.split(":"):
            try:
                if len(octet) > 4 or octet[0].isspace():
                    return self.NONE
                num = int(octet, 16)
                if num > 2**16 or num < 0:
                    return self.NONE
            except Exception:
                return self.NONE
        return self.IP6

    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count(".") == 3:
            return self.isIP4(queryIP)
        elif queryIP.count(":") == 7:
            return self.isIP6(queryIP)
        else:
            return self.NONE


if __name__ == "__main__":
    s = Solution()
    print(s.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
