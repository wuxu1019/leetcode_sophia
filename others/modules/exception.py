def test():
    try:
        i = 3/0 
    except Exception, msg:
        print "here is some error, see below for details"
        print msg

test()
