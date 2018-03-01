"""
*args and **kwargs are mostly used in function definitions. *args and **kwargs allow you to pass a variable number of arguments to a function. What does variable mean here is that you do not know before hand that how many arguments can be passed to your function by the user so in this case you use these two keywords. *args is used to send a non-keyworded variable length argument list to the function.

"""

def test1(*args):
    for a in args:
        print a

def test2(**kwargs):
    for k, v in kwargs.iteritems():
        print k , v

data1 = [1, 2, 3, 4, 5]
data2 = [3, 4, 5]
print "1 test"
test1(*data1)
print "2 test"
test1(data2)

data3 = {'a': 1, 'b': 4}
print "3 test"
test2(**data3)
print "4 test"
test2(name = 'jeff', age = 10, sex = 'male')

data1 = (1, 2)
print "5 test"
test1(*data1)

data1 = set([4, 5])
print "6 test"
test1(*data1)
