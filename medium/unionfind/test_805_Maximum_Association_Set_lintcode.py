"""
Description
Amazon sells books, every book has books which are strongly associated with it. Given ListA and ListB,indicates that ListA [i] is associated with ListB [i] which represents the book and associated books. Output the largest set associated with each other(output in any sort). You can assume that there is only one of the largest set.

The number of books does not exceed 5000.
Have you met this question in a real interview?
Example
Given ListA = ["abc","abc","abc"], ListB = ["bcd","acd","def"], return["abc","acd","bcd","dfe"].

Explanation:
abc is associated with bcd, acd, dfe, so the largest set is the set of all books
Given ListA = ["a","b","d","e","f"], ListB = ["b","c","e","g","g"], return ["d","e","f","g"].

Explanation:
The current set are [a, b, c] and [d, e, g, f], then the largest set is [d, e, g, f]
"""
import collections

class Solution:
    """
    @param ListA: The relation between ListB's books
    @param ListB: The relation between ListA's books
    @return: The answer
    """
    def maximumAssociationSet_set(self, ListA, ListB):
        # Write your code here
        relation = collections.defaultdict(list)
        for i in range(len(ListA)):
            a, b = ListA[i], ListB[i]
            relation[a].append(b)
            relation[b].append(a)
        groups = []
        for k, v in relation.items():
            if k in relation:
                group = set([k])
                queue = collections.deque([k])
                while queue:
                    node = queue.popleft()
                    if node in relation:
                        queue.extend(relation[node])
                        group |= set(relation[node])
                        del relation[node]
                groups.append(group)
        ans = max(groups, key=lambda k:len(k))
        return list(ans)

    def maximumAssociationSet_union_find(self, ListA, ListB):
        fa = range(0, 5001)
        cnt = [1] * 5001
        strlist = {}
        dict = {}

        def gf(u):
            if fa[u] != u:
                fa[u] = gf(fa[u])
            return fa[u]

        tot = 0
        for i in range(0, len(ListA)):
            a, b = 0, 0
            if ListA[i] not in dict:
                tot += 1
                dict[ListA[i]] = tot
                strlist[tot] = ListA[i]
            a = dict[ListA[i]]
            if ListB[i] not in dict:
                tot += 1
                dict[ListB[i]] = tot
                strlist[tot] = ListB[i]
            b = dict[ListB[i]]
            x, y = gf(a), gf(b)
            if x != y:
                fa[y] = x
                cnt[x] += cnt[y]
        ans = []
        k, flag = 0, 0
        for i in range(0, 5001):
            if k < cnt[gf(i)]:
                k = cnt[gf(i)]
                flag = gf(i)
        for i in range(0, 5001):
            if gf(i) == flag:
                ans.append(strlist[i])
        return ans

    def maximumAssociationSet_union_find2(self, ListA, ListB):

        flag = range(0, 5001)

        def findflag(num):
            if flag[num] == num:
                return num
            return findflag(flag[num])


        name_numb = {}
        numb_name = {}
        tot = [1] * 5001
        ct = 0
        for i in range(len(ListA)):
            a, b = ListA[i], ListB[i]
            if a not in name_numb:
                ct += 1
                name_numb[a] = ct
                numb_name[ct] = a
            a = name_numb[a]

            if b not in name_numb:
                ct += 1
                name_numb[b] = ct
                numb_name[ct] = b
            b = name_numb[b]

            x, y = findflag(a), findflag(b)
            if x != y:
                flag[y] = x
                tot[x] += tot[y]
        ans = []
        k, f = 0, 0
        for i in range(1, 5001):
            sm = tot[findflag(i)]
            if k < sm:
                k, f = sm, findflag(i)
        for i in range(1, 5001):
            if findflag(i) == f:
                ans.append(numb_name[i])

        return ans




if __name__ == '__main__':
    s = Solution()
    ListA = ["abc","abc","abc"]
    ListB = ["bcd","acd","def"]
    rt1 = s.maximumAssociationSet_set(ListA, ListB)
    print rt1

    rt2 = s.maximumAssociationSet_union_find2(ListA, ListB)
    print rt2