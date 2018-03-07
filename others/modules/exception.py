
def IsEqual(a, b):

    if len(a) != len(b):
        raise Exception('{} is not the same as {}'.format(a, b))
    for i in range(len(a)):
        if a[i] != b[i]:
            raise Exception('{} is not the same as {}'.format(a, b))
    print '{} is the same as {}'.format(a, b)

def test():
    try:
        i = 3/0 
    except Exception, msg:
        print "here is some error, see below for details\n\n"
        print msg
    finally:
        print "Must go to here"
        IsEqual('bcc', 'bcc')

test()
