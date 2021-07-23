class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHi(self):
        print("Hello my name is %s" % self.name)

    def sayAge(self):
        print("I am %s years old" % self.age)

    def sayBDay(self, bDay):
        print("My birthday is %s" % bDay)

    def sayNumKids(self, numKids):
        print("I have %d kids" % numKids)

def introduce(person):
    person = Person(person.name, person.age)
    person.sayHi()
    person.sayAge()
    person.sayBDay("June 17th")
    person.sayNumKids(17)

def main():
    p1 = Person("John", 36)
    introduce(p1)

main()
