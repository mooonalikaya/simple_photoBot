
# class Animal:
#     def __init__(self,name,view):
#         self.name = name
#         self.view = view
#         print(self.__get_info())

#     def get_name(self):
#         return self.name
#     def get_view(self):
#         return self.view
#     def __get_info(self):
#         return f"{self.name} {self.view}"
    
    
# cat=Animal("Kitty","mysyk")


#get_name-public method
# _get_name-protected method-запускается в критических моментов
# __get_name-private method- приватный запускается только внутри класса



# class Teffalle:
#     def turn_on(self):
#         print("Включения")
#         print(self.__water())
#         print(self.__water_down())
#         print(self._turn_off())


#     def __water(self):
#         return"Вода на стадии кипение"
#     def __water_down(self):
#         return"Вода закипела"
#     def _turn_off(self):
#         return"Выключения"
    
# a=Teffalle()
# print(a.turn_on())
# print(a._turn_off())



class A:
    def __find(self):
        return("asas")
    
    def _find(self):
        return"shsh"
    def find(self):
        return "lplp"
    
a=A()
print(a.find())
print(a._find())


