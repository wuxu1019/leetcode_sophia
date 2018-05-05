"""
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].

"""

import collections

class DSU(object):
    def __init__(self):
        self.p = range(1001)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.p[self.find(y)]

class Solution(object):
    def accountsMerge_set(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        record = collections.defaultdict(list)
        for account in accounts:
            k, v = account[0], set(account[1:])
            if k not in record:
                record[k].append(v)
            else:
                update = []
                for g in record[k]:
                    if v & g:
                        v |= g
                    else:
                        update.append(g)
                update.append(v)
                record[k] = update
        return [[k] + sorted(list(v)) for k, l in record.items() for v in l]

    def accountsMerge_dfs(self, accounts):
        emil_acc = collections.defaultdict(list)
        for i, account in enumerate(accounts):
            for e in account[1:]:
                emil_acc[e].append(i)
        visited = [False] * 1001

        def dfs(i, record):
            if visited[i]:
                return
            visited[i] = True
            for email in accounts[i][1:]:
                record.add(email)
                for acc in emil_acc[email]:
                    dfs(acc, record)

        ans = []
        for i, account in enumerate(accounts):
            if visited[i]:
                continue
            name, record = account[0], set()
            dfs(i, record)
            ans.append([account[0]] + sorted(list(record)))
        return ans

    def accountsMerge_unionfind(self, accounts):
        id = 0
        email_id = {}
        email_name = {}
        dsu = DSU()

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_name[email] = name
                if email not in email_id:
                    email_id[email] = id
                    id += 1
                dsu.union(email_id[account[1]], email_id[email])

        ans = collections.defaultdict(list)
        for email in email_name:
            ans[dsu.find(email_id[email])].append(email)

        return [[email_name[i[0]]] + sorted(i) for i in ans.values()]


if __name__ == '__main__':
    s = Solution()
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    rt1 = s.accountsMerge_dfs(accounts)
    print rt1

    rt2 = s.accountsMerge_unionfind(accounts)
    print rt2

