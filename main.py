class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f'Имя: {self.name}, возраст {self.age}')


person_1 = Person('Василий', 25)
print(person_1.name, person_1.age)
person_1.info()

# try:
#     person_1.info()
# except ZeroDivisionError:
#     print('ZeroDivisionError')
# #else:
#     #print('/0')
#     person_1.info()


class Square:
    def __init__(self, a):
        self.a = a
    def per(self):
        print(f'Периметeр: {self.a*4}')
    #def __init__(self, p):
    def area(self):
        print(f'Площадь: {self.a**2}')



square_1 = Square(5)
square_1.area()

square_1 = Square(10)
square_1.per()


class rectangle:
    def __init__(self, c, k):
        self.c = c
        self.k = k
    def __pe(self, c, k):
        print(f'Периметр: {(self.c+self.k) *2}')
    def pl(self, c, k):
        print(f' Площадь: {self.k*self.c}')
    #def l(self, k):
        #print(f'Площадь: {self.c+k}')



rectangle_1 = rectangle(5, 10)
rectangle_1._rectangle__pe(5, 10)


rectangle_2 = rectangle(15, 16)
rectangle_2.pl(15, 16)

class nikolay:
    __slots__ = ['name', 'age']
    def __init__(self, name, age):
        if name == 'Николай':
            self.name = name
        else:
            self.name = f'Я не {name}, я Николай'
        self.age = age

nikolay_1 = nikolay('Джастин', 16)
print(nikolay_1.name)

#nikolay_1.info()

class Mammal:
    def __init__(self, type_animal, name_animal):
        self.type_animal = type_animal
        self.name_animal = name_animal

class Cat(Mammal):
    def info(self):
        return f'Кошка: {self.type_animal}, {self.name_animal}'

S1 = Mammal('Кошачьи', 'dyson')
S2 = Cat('Кошачьи', 'dyson')
print(S2.info())

