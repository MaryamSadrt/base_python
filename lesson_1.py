a = 5
b = 6
NAME = "maryam"
# a = 24
#ghbdtn
#ctrl+/ - выделить и закомментировать

#Если большими буквами, то это константа, но ее можно менять

print (a)
print (a+b)
print (a-b)
print (a*b)
print (a/b)
print(a**b)
print(a%b)
print("Hello")
print('Hi')

print(f"Hello. a = {a}") # форматированный вывод данных
print(f"Hello. a + b = {a+b}")

"""
ghjkl
ghjk
hjk
dsghj
"""
c = 5.7
d = 7.0

print(type (a))
print(type(c))
print(type(a+c))
# boolean
print(7==10)
print(7>=10)
print(7<=10)
print(7!=10)

#string
age = "24"
print(age + "1")
print(int(age) + 1) #int преобразует в число
last_name = ("Ivanov"
             "bnvcxz"
             "fgdszsz")
text = """
vghcf
vgcx
vcvbxc
"""
city = "Moscow\n city" #\n символ переноса строки
print(city)

#списки
numbers = [] # пустой список (как массив)
new_numbers = [1,2,3]
# нумерация начинается с нуля 0  1  2  3
elements = [1, "2", "name", True, [1,2,3]]
print(elements)
cars = list() # тоже список, но лучше использовать литералы []

#кортеж - неизменный список tuple или ()
colors = tuple ()
new_colors = ("red", "blue", "green")

#словарь, ассоциированный массив (как объект в js)
car = {}
my_car = dict ()
# хранит данные в формате "ключ": значение
info = {"name": "Misha",
        "age": 26,
        "city": "Moscow",
        25: 46,
        ("1", 2, 3): 24,
        }
print(info)
# в словаре не может быть двух одинаковых ключей
# ключом в словарях может быть только неизменяемый тип данных

# set - множества
set_of_names = {"Masha", "Sasha", "Dima", "Masha"}
print(type(set_of_names))
print(set_of_names)

cars = ["bmw", "audi", "bmw", "bmw"]
# list > set
print(list(set(cars)))
txt = "hello"
print(list(txt))
print(set(txt))

#управляющие конструкции
# if - elif - else
age = 0
if (age < 11 and age != 0):
    print("error")
elif age == 0:
    print ("age = 0")
else:
    print("ok")

print ("Next block")

in_name = input("Введите ваше имя: ")
in_age = input("Введите ваш возраст: ")

print(f"Ваше имя - {in_name}")
print(f"Ваш возраст- {in_age}")
print(type(in_age))
