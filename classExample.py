'''
Class
	A class is a blueprint for the object.

An object has two characteristics:
		attributes
		behavior

Let's take an example:
Parrot is an object,
		name, age, color are attributes
		singing, dancing are behavior

class ClassName(object):
    --snip--

Making an Instance from a Class
objectName = ClassName(arguments)    

'''

class MyClass:
    """This is my first class"""
    a= 10

    def myMethod(self):
        print('Hello Word')

print(MyClass.a)
print(MyClass.myMethod)
print(MyClass.__doc__)
print(MyClass.__name__)
print(MyClass.__base__)

myobj = MyClass()
print(myobj.a)
myobj.myMethod()


class Parrot:

    species = 'bird'

    def __init__(self,name,age) -> None:
        print('This is a Instance attrbute')
        self.name=name
        self.age= age

tia = Parrot('Moti',2)
print(tia.species)

print(f'Name : {tia.name} and Age: {tia.age}')


class Parrot:
    def fly(self):
        print('Parrot can fly')

    def swim():
        print('Parrot can\'t swim')

class Penguin:
    def fly(self):
        print('Penguin can\'t fly')

    def swim():
        print('Penguin can swim')

def flying_test(obj):
    obj.fly()

pr = Parrot()
pg = Penguin()

flying_test(pr)
flying_test(pg)


class Computer:

    def __init__(self) -> None:
        self.__maxPrice = 900

    def getMaxPrice(self):
        print(f'Selling Price : {self.__maxPrice}')

    def setMaxPrice(self,price):
        self.__maxPrice = price

c = Computer()
c.getMaxPrice()

c.__maxPrice=1000
c.getMaxPrice()

c.setMaxPrice(2000)
c.getMaxPrice()

class Bird:
    def __init__(self) -> None:
        print('Bird is ready')

    def whoIsThis(self):
        print("I am a bird")

    def swim(self):
        print("Swim faster")


class Penguin(Bird):

    def __init__(self) -> None:
        super().__init__()
        print('Penguin is Ready')

    def whoIsThis(self):
        print("I am a Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoIsThis()
peggy.swim()
peggy.run()


class Person:

    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def walk(self):
        print(f'{self.name.title()} is now walking')

    def run(self):
        print(f'{self.name.title()} is now running')
        
    def show(self):
        s = self.name + ' ' + str(self.age)

class Student(Person):
    def __init__(self, name, age,fees) -> None:
        super().__init__(name, age)
        self.fees = fees

    def __str__(self) -> str:
        return f'{self.name} {self.age} {self.fees}'

s1 = Student('Meem',17,2000)
print(s1)








    












