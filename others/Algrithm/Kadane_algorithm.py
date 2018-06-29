"""
to find largest continues sum of sub array

For example, in the array [-5, 6, 7, 1, 4, -8, 16], the maximum sum is 26.
That is because adding 6 + 7 + 1 + 4 + -8 + 16 gives us 26.
"""

def kadane(l):
    if not l:
        return None
    cur_max = global_max = 0
    for i in l[1:]:
        cur_max = max(cur_max+i, i)
        global_max = max(global_max, cur_max)
    return global_max

if __name__ == '__main__':
    l = [-5, 6, 7, 1, 4, -8, 16]
    rt = kadane(l)
    print rt