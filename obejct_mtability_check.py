class Person:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

def greet(person):
    person.name="ankit"
    return person

p=Person("nitish","male")
p1=greet(p)
print(id(p))
print(id(p1))
