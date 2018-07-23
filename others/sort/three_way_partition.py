
def three_way_partition(l, mid):
    i, j = 0, 0
    n = len(l) - 1
    while j <= n:
        if l[j] < mid:
            l[i], l[j] = l[j], l[i]
            i, j = i + 1, j + 1
        elif l[j] > mid:
            l[j], l[n] = l[n], l[j]
            n -= 1
        else:
            j += 1
    print i, j, n
    return l

if __name__ == '__main__':
    l = [3,2,3,3,2,1,1,2,3,1,1,3,2,1,2,2,2,2,1]
    mid = 2
    rt = three_way_partition(l, mid)
    print rt