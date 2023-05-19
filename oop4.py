class Animal:
    def __init__(self, name):
        self.name = name
   
    def voice(self):
        return("какой то звук")

    def get_name(self):
        raise NotImplementedError(
            "Метод get_name() должен быть реализован в подклассе")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def voice(self):
        return("мяу")
    
    def get_name(self):
        return self.name
    
    
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def voice(self):
        return("гав")

    def get_name(self):
        return self.name
# Нельзя создать экземпляр абстракного класса Animal
# animal = Animal("Какое-то животное")

cat1 = Cat("Cat")
dog1 = Dog("Dog")

a = [cat1, dog1]

for i in  a:
    print(i.voice())
    #абстрактный класс-при проверке дочерних классов есть ли методы (на валидацию)
    
#----------------------------------------------------------------------------------------