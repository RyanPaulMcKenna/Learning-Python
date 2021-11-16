import copy

org = [0,1,2,3,4,5]
nested = [[0,1,2,3,4,5],[6,7,8,9,10]]

# only copies one level of nesting
cpy = copy.copy(org)

# deep copy requires for multi level copy
deep = copy.deepcopy(nested)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person('Alex',28)
p2 = p1

p2.age = 30

print(p1.age)
print(p2.age)

class Company:
    def __init__(self,boss, employee):
        self.boss = boss
        self.employee = employee

company = Company(p1,p2)

#deep is needed p1 & p2 will still be linked
company_clone = copy.deepcopy(company)

print(company_clone.boss.age)
print(company.boss.age)
