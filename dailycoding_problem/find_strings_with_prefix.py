"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

"""

class TrieNode(object):
    def __init__(self):
        self.end = False
        self.next = {}


def find_strings(l, target):
    head = TrieNode()

    for s in l:
        insertString(head, s)
    ans = []
    p = head
    for c in target:
        if c in p.next:
            p = p.next[c]

    def dfs(head, base):
        if head.end == True:
            ans.append(base)
        for k, v in head.next.items():
            dfs(v, base+k)
    dfs(p, target)
    return ans


def insertString(head, s):
    p = head
    for c in s:
        if c not in p.next:
            p.next[c] = TrieNode()
        p = p.next[c]
    p.end = True

if __name__ == '__main__':
    l = ['dog', 'deer', 'deal', 'de', 'deroo', 'de']
    target = 'de'
    ans = find_strings(l, target)
    print ans
