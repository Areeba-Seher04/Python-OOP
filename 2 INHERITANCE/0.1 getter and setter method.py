
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self,name):
        self.name = name

    def set_age(self,age):
        self.age = age

    


Areeba = Person("Areeba",100)

print("name: ",Areeba.get_name())
print("age: ",Areeba.get_age())


Areeba.set_name("Areeba Seher")
print(Areeba.get_name())
