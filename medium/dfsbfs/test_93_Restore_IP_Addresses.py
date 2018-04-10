"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)


"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.rt = []

        def restoreIpAddressesHelper(i, p, base):
            if p < 4 and i >= len(s):
                return

            if p == 4:
                if i == len(s):
                    self.rt.append(base[:-1])
                return

            for j in range(1, 4):
                sub = s[i:i + j]
                if int(sub) <= 255:
                    restoreIpAddressesHelper(i + j, p + 1, base + sub + '.')
                if sub[0] == '0':
                    break

        restoreIpAddressesHelper(0, 0, '')
        return self.rt

if __name__ == '__main__':
    s = Solution()
    string = '25525511135'
    rt1 = s.restoreIpAddresses(string)
    print rt1