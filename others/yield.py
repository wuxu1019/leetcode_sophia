def generate():
    mylist = range(3)
    for i in mylist:
        yield i ** 2

my_generate = generate()
print my_generate
my_generate.next()
my_generate.next()
