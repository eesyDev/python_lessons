# a = [1, 3, 6, 7, 9, True, False, [1, 2, 3]]

# print(a[4])
# print(a.index(7))
# print(a[:6])
# print(a.index(9))

# print(a[-1][1])


class_a = [12, 34, 90, 87, 11, 68, 56]

class_a.append(2)
team_1 = class_a[::2]
team_2 = class_a[1::2]

team_1.remove(90)

print(team_1, team_2)

team_1.extend(team_2)

team_1.sort()


# PROBLEM 0
# Создать пустой список и добавьте 5 кортежей.


empty_list = []

cortage_1 = (1, 2, 3)
cortage_2 = (2, 4, 6)
cortage_3 = (3, 7, 9)
cortage_4 = (6, 9, 0)
cortage_5 = (5, 6, 7)

empty_list.append(cortage_1)
empty_list.append(cortage_2)
empty_list.append(cortage_3)
empty_list.append(cortage_4)
empty_list.append(cortage_5)


print(empty_list)


# PROBLEM 1
# Создать Tuple из 3 элементов и вывести каждый из них по индексу.


t = ('one', 'two', 'three')
print(t[0], t[1], t[2])


# PROBLEM 2
# Создать Лист и заполнить его 5 РАЗНЫМИ ТИПАМИ ДАННЫХ.

list_list = []

string = 'Some string'
integer = 456
floater = 9.94900
lister = ['e', 't']
tupler = (0, 0, 1, 0)

list_list.append(string)
list_list.append(integer)
list_list.append(floater)
list_list.append(lister)
list_list.append(tupler)

print(list_list)


# PROBLEM 3
# 1.Создать Лист из 5 разных имён.
# 2.Создать пустую строку и через .join() соеденить пустую строку и все имена в списке.


name_list = ['Name1', 'Name2', 'Name3', 'Name4', 'Name5']

empty_string = ' '

a = empty_string.join(name_list)

print(a)


# PROBLEM 4
# Создать 2 списка(List) заполнить данными,
# к первому списку добавить все объекты второго списка


list1 = [1, 4, 'Hello']
list2 = ['Team', 4, 6]
list1.extend(list2)

print(list1)


# PROBLEM 5
# # Лист №1:
# names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon']

# Взять Лист №1 из посчитать сколько раз там встречается имя "Jack".


names = ['Jack', 'Jimmy', 'Jackson', 
        'Jhon', 'Jackson', 'Jhon',  'Jimmy',
         'Jackson', 'Jhon', 'Jack', 'Jimmy', 'Jack',
          'Jackson', 'Jhon', 'Jackson', 'Jhon',
           'Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon']


how_much = names.count('Jack')

print(how_much)

# PROBLEM 6
# # Лист №1:
# names = ['Jack', 'Jimmy', 'Oskar', 'Jhon', 'Jackson', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon']
# Удалить из Листа №1 объект "Oskar"

names_1 = ['Jack', 'Jimmy', 'Oskar', 'Jhon', 'Jackson', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon']


names_1.remove('Oskar')

print(names_1)

# PROBLEM 7
# Создать пустой лист.
# Добавить в него сначала Ваше Имя, Год Рождения, любимый Язык Программирования.


data = []

my_name = 'Rano'
year_of_birth = 1991
languge = 'JavaScript'

data.append(my_name)
data.append(year_of_birth)
data.append(languge)

print(data)


# PROBLEM 8
##LIST №2

# Взять Лист №2 узнать индекс объекта(строки) "loop" и удалить его по индексу 


python_list = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]

loop_loop = python_list.index('loop')
python_list.pop(loop_loop)

print(python_list)


# PROBLEM 9
# Лист №3 
# numbers = [123, 321, 2, 543]
# Взять Лист №3 и посчитать произведение этих чисел т.е. умножить их все и вывести результат.

numbers = [123, 321, 2, 543]

mult = numbers[0] * numbers[1] * numbers[1]

print(mult)



# создайте 2 пустых листа
# list_1 = []
# list_2 = []
# спросите у пользователя 5 чисел
# если он четный добавте его в первый список
# иначе на другой
# в конце вывести оба списока

list_1 = []
list_2 = []

num_1 = int(input('Enter some num: '))
num_2 = int(input('Enter some num: '))
num_3 = int(input('Enter some num: '))
num_4 = int(input('Enter some num: '))
num_5 = int(input('Enter some num: '))


if num_1 % 2 == 0:
    list_1.append(num_1)
else:
    list_2.append(num_1) 


if num_2 % 2 == 0:
    list_1.append(num_2)
else:
    list_2.append(num_2) 

if num_3 % 2 == 0:
    list_1.append(num_3)
else:
    list_2.append(num_3)

if num_4 % 2 == 0:
    list_1.append(num_4)
else:
    list_2.append(num_4)

if num_5 % 2 == 0:
    list_1.append(num_5)
else:
    list_2.append(num_5)   

print(list_1, list_2)

# № 2
# создайте 1 лист
# спросите у пользователя 5 чисел и добавте его в список 
# и определите самое большое и самое маленькое и среднее арифметическое


user_list = []


num2_1 = int(input('Enter some num: '))
num2_2 = int(input('Enter some num: '))
num2_3 = int(input('Enter some num: '))
num2_4 = int(input('Enter some num: '))
num2_5 = int(input('Enter some num: '))

user_list.append(num2_1)
user_list.append(num2_2)
user_list.append(num2_3)
user_list.append(num2_4)
user_list.append(num2_5)

length_list = len(user_list)

print(max(user_list))
print(min(user_list))
print(sum(user_list) // length_list)


# № 3
# создайте пременное 
# products = [
#   'яблоко', 
#   'груша', 
#   'арбуз',
#   'банан', 
#   'мандарин'
# ]
# распечатайте его на экране 
# пусть пользователь быверит индекс товара
# после удалите товар из products
# если пользователь ввел индекс которого нет 
# скажите что он не правильно ввел индекс
# 

products = [
  'яблоко', 
  'груша', 
  'арбуз',
  'банан', 
  'мандарин'
]


print(products)

choise_index = int(input("Choose a num: "))

prod_len = len(products)
print(prod_len)


if choise_index < prod_len - 1:
    products.pop(choise_index)
    print(products)
else:
    print('Incorrect num')


# № 4
# тест
# создайте переменный points = 0
# спросите у пользователя вопрос с 3 ответами  
# если пользователь выберит правильный вариант тогда в переменный points =  + 1 
# 
# создайте 4 таких вопроса  
# в конце распечатайте points
# в итоге если ответ будет равен или больше 3
# скажите "вы прошли тест"
# а если результат будет равен 1 или 2
# скажите "вы провалили тест попробуйте след раз"
# иначе скажите "вы не от ветили ни на один вопрос"


points = 0

question1 = input('Question 1; a1, a2, a3: ')
question2 = input('Question 1; a1, a2, a3: ')
question3 = input('Question 1; a1, a2, a3: ')
question4 = input('Question 1; a1, a2, a3: ')

if question1 == 'a1':
    points += 1

if question2 == 'a2':
    points += 1

if question3 == 'a1':
    points += 1
else:
    pass

if question4 == 'a3':
    points += 1
else: 
    pass

if points >= 3:
    print('You pass the test')
elif points == 1 or points == 2: 
    print('Try next time')
else:
    print('You didnt answere')


# № 5
# создайте лист с длиной 10 значений  
# спромите у пользователя цифру от одного до 9
# выведите ему лист от числа которого он вел до конца


list_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

user_num = int(input('Put some num 1 - 9: '))

print(list_10[user_num:])

# № 6
# Подтверждения пороля 
# спросите у пользователя логин и пороль и подтверждения пороля
# создайте условие где проверяется логин он должен состоять и из цифр и из букв. пример 'aktan2002' (используйте isdigit() и isaplha() для проверки)
# cоздайте условие где проверяется пороль он должен совпадать с подтверждением пороля
# если пройдет все проверки тогда сохраните в списке users. пример users = [('aktan2002', 'qwerty'),('ilim12', '12345')]

login = input('isert your login: ')
password = input('enter your password: ')
password_confirm = input('confirm your password: ')
users = []

if not login.isdigit() and not login.isalpha():  
    if password == password_confirm:
        users.append((login, password))
else: 
    pass


print(users)














