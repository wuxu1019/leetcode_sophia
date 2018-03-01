import csv
from collections import namedtuple

Company = namedtuple('Company', 'name, location, contry, zipcode')
print Company._fields
data = []
for ctr in map(Company._make, csv.reader(open("company.csv", "rb"))):
    print ctr.name, ctr.location
    data.append(ctr)
c1 = data[0]
print c1
print "change the some data"
c2 = c1._replace(name='NV')
print c1, c2

