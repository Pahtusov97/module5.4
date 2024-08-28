# class Example:
#   def __new__(cls, *args, **kwargs):
#     print(args)
#     print(kwargs)
#     return object.__new__(cls)
#
#   def __init__(self, first, second, third):
#     print(first)
#     print(second)
#     print(third)
#
# ex = Example('data', second=25, third=3.14)
class House:
    houses_history = []
    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)
        

    def __init__(self, name, Nazvanie):
        self.name = name
        self.Nazvanie = Nazvanie

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
print(House.houses_history)
del h2
del h3
