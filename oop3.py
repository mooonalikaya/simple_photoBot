
# class Car:
#     def __init__(self,country,marka,model,color):
#         self.country=country
#         self.marka=marka
#         self.model=model
#         self.color=color
        
#     def voice(self):
#         return"биб"
    

# class Cat:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color

#     def voice(self):
#         return"мяу"

# class Bird:
#     def __init__(self,name,color):
#         self.name=name
#         self.color=color

#     def voice(self):
#         return "чирик"    

# #полимарфизм
# bmw=Car("BMW","Germany","M5","Black")
# koshka=Cat("Kitty","red")
# ptichika=Bird("Орёл","blue")

# print([i.color for i in [bmw,koshka,ptichika]])

# #наследование это
# class Animals:
#     def __init__(self,type,name,color,age,gender):
#         self.type=type
#         self.name=name
#         self.color=color
#         self.age=age
#         self.gender=gender
        
# class Cat(Animals):
#     def __init__(self,type:str,name:str,color:str,age:int,gender:str):
#         super().__init__(type,name,color,age,gender)
#     def get_models(self):
#         text="все знаение:\n"
#         for k,v in list (self.__dict__.items()):
#             text+=f"{k}: {v}\n"
#         return text

# koshka=Cat("mysyk","beka","white",3,"male")
# print(koshka.get_models())
# #----------------------------------------------
# class Dog:
#     def __init__(self,type,name,color,age,gender):
#         self.type=type
#         self.name=name
#         self.color=color
#         self.age=age
#         self.gender=gender

# class Cat(Dog):
#     def __init__ (self,type,name,color,age,gender):
#         super().__init__(type,name,color,age,gender)

# class Bird(Dog):
#     def __init__ (self,type,name,color,age,gender):
#         super().__init__(type,name,color,age,gender)

# koshara=Cat("mysyk","beka","white",3,"male")
# mikky=Dog("it","barsik","red",6,"female")
# lala=Bird("kus","lili","blue",1,"male")
# print([i.color for i in [koshara,mikky,lala]])

#----------------------------------------------

# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def voice(self):
#         return "sound"
    
#     def __str__(self):
#         return "self.name"
    
# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def voice(self):
#         return "meow"
    
# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def voice(self):
#         return "woof"
    
# a=Dog("beka")
# b=Cat("kitty")
# c=Animal("k")


# model=[a,b]
# for i in model:
#     print(i.voice())


# #---------------------
# class Animal:
#     def init(self, name) -> None:
#         self.name = name
    
#     def voice(self):
#         return "Какой-то звук"
    
#     def str(self) -> str:
#         return f"Я взял имя у родителя: {self.name}"

# class Cat(Animal):
#     def init(self, name) -> None:
#         super().init(name)
    
#     def voice(self):
#         return "Мяу мяу"

# class Dog(Animal):
#     def init(self, name) -> None:
#         super().init(name)
    
#     # def voice(self):
#     #     return "Гав гав"

#-----------------------------
class Technology:
    def __init__(self,name,model):
        self.name=name
        self.model=model

class Cars(Technology):
    def init(self,name,model):
        super().__init__(name,model)

class Phones(Technology):
    def init (self,name,model):
        super().__init__(name,model)
        
a=Technology("Технологии","модель")
b=Cars("bmw","m5")
c=Phones("Iphone","11promax")

print([i.name for i in [a,b,c]])
print([i.model for i in [a,b,c]])


