# class Country:
#     def __init__(self,title,popilation,president,capital,width,height,language):
#         self.title=title
#         self.population=popilation
#         self.president=president
#         self.capital=capital
#         self.width=width
#         self.height=height
#         self.language=language

#     def __str__ (self):
#         return  f"Это класс который отвечает создание стран {self.title}"


# kz=Country ("Kazakhstan","19млн","K.Zh.Tokaev","Astana","100px","80px","qazaq")
# kg=Country ("Kyrgyzstan","6млн","S.Zhaparov","Bishkek","20px","20px","kyrgyz")

# print(kg)

#cat,dog,animals
#name,poroda,age,color,pown,tail,gender


#Country     
#title,popilation,capital,president,width,height,language,


class Animal:
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color

    def get_name(self):
        return f"Меня зовут {self.name}"


    def __str__ (self):
        return f"Животное {self.name}"
    
cat=Animal("Kitty","10","brown")
dog=Animal("Barsik","20","white")

print(dog.get_name())



