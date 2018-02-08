"""
when the data is very big, can not put into memory in one time, 
how to rotate data

use a table to record all the data in disk, like:
table = [[0, 0], [1 100], [2, 200] ... [MAX, location]]
[index, location]
let us suppose all the metadata has the same size
k is rotate steps
read() is used to read metadata from disk to memory
write() is used to write metadata from memory to dish
"""

def rotateBigData(table, size, k):
    blk_rotate, part_rotate = divmod(k, size)
    blk_rotate = blk_rotate % len(table)
    for block in table:
        block[0] = (block[0] + len(table)-blk_rotate)%len(table)
    prev = read(table[-1][-part_rotate])

    ct = 0
    while ct < len(table):
        current = read(table[ct])
        temp = current[-part_rotate:]
        current[part_rotate:] = current[:-part_rotate]
        prev = temp
        write(table[ct], current)
    
    return
    



