class Person(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    @classmethod
    def fromid(cls, name, id):
        return cls(name, 'NO:'+id)

    @staticmethod
    def fromname(name, id):
        return Person(name, 'Number:'+id)

    def introduce(self):
        print "my name is {}, my id is {}".format(self.name, self.id)

class Student(Person):
    age = '18'

if __name__ == '__main__':
    d = Person.fromid('Sophia', '1019')
    d.introduce()


    f1 = Student.fromid('John', '1234')
    f2 = Student.fromname('John', '1234')
    print type(f1)
    print type(f2)
    f1.introduce()
    f2.introduce()