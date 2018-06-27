
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
    l = [1, 4, 1, 3, 4, 6, 2, 3, 4, 5, 6]
    mid = 4
    rt = three_way_partition(l, mid)
    print rt