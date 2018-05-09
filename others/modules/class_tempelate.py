class Person(object):

    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age

    def str(self):
        return self.firstname + " " + self.lastname + ", " + str(self.age)

class Employee(Person):

    def __init__(self, first, last, age, staffnum):
        super(Employee, self).__init__(first, last, age)
        self.staffnumber = staffnum

    def str(self, tail):
        return super(Employee, self).str() + ", " +  self.staffnumber + tail


x = Person("Marge", "Simpson", 36)
y = Employee("Homer", "Simpson", 28, "1007")

print(x.str())
print(y.str(' ok'))
