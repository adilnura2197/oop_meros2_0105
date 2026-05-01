class Animal:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    def eat(self):
        print(f"{self.name} ovqat yeyapdi")

class Dog(Animal):
    def __init__(self, name, age, type, bread, color):
        super().__init__(name, age, type)
        self.bread = bread
        self.color = color

    def eat(self):
        super().eat()
        print(f"Tez yeyapdi")

    def bark(self):
        print(f"{self.name} hurmoqda")


a1 = Dog("It", 3, 'hayvon', "ovqat", "oq")
a1.eat()
a1.bark()
