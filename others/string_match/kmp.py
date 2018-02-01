"""
good video about KMP search
https://www.youtube.com/watch?v=GTJr8OvyEVQ
good explaination about KMP search
https://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
"""
def computePatternTable(pat):
    pTable = [0]
    i, j = 1, 0
    while i < len(pat):
        if pat[i] == pat[j]:
            j += 1
            pTable.append(j)
            i += 1
        else:
            if j != 0:
                j = pTable[j-1]
            else:
                pTable.append(0)
                i += 1
    return pTable

def KMPSearch(pat, txt):
    pTable = computePatternTable(pat)
    print pTable
    i, j = 0, 0
    rt = []
    while i < len(txt):
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == len(pat):
           rt.append(i-j)
           j = pTable[j-1]
        elif i < len(txt) and pat[j] != txt[i]:
           if j != 0:
               j = pTable[j-1]
           else:
               i += 1
    return rt     

pattern = 'AABAABAAA'
pTable = computePatternTable(pattern)
print "Test pTable"
print "Input is {0} and pattern table is {1}".format(pattern, pTable)

txt = "AAAAABAAABA"
pattern = "AAB"
rt = KMPSearch(pattern, txt)
print "Test KMP search"
print "Found match on {0}".format(rt)


