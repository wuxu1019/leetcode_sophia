import hashlib
import collections
import os

def readfolder(path)
    allitems = os.listdir()
    rt = []
    for i in allitems:
        item = os.path.join(path, i)
        if os.path.isfile(item):
           rt.append(item)
        else:
            rt.extend(readfolder(item))
    return rt

def md5_file(f, chunk_size=1024):
    hash = hashlib.md5()
    with open(f, 'rb') as ph:
        chunk = ph.read(chunk_size)
        while chunk:
            hash.update(chunk)
            chunk = ph.read(chunk_size)
    return hash.hexdigest()

def comparefiles(f1, f2):
    try:
        p1 = open(f1, 'rb')
    except Exception, msg:
        print 'Not able to open {0}'.format(f1)
        print msg
    try:
        p2 = open(f2, 'rb')
    except Exception, msg:
        print 'Not able to open {0}'.format(f2)
        print msg

    for i in p1:
        for j in p2:
            if i != j:
                return False
    if not p1.read() and not p2.read():
        return True
    return False

def findduplicates_way1(path):
    files = readfolder(path)
    md5_table = collections.defaultdict(list)
    for f in files:
        md5_table[md5_file(f)].append(f)
    return [i for i in md5_table.values() if len(i) > 1]

def findduplicates_ways(path):
    files = readfolder(path)
    dup = collections.defaultdict(list)
    while files:
        target = files.pop()
        for f in files:
            if comparefiles(target, f):
                dup[target].append(f)
    return [ [k] + v for k, v in dup.items()]

if __name__ == '__main__':
    rt = findduplicates_way1(path)