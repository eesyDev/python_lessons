a = set()

print(a)

#methods

#add
a.add(2)
a.update([1, 44, 7])

#remove

a.pop() #randome

a.remove(2)
a.clear() #clean all
#a.discard() #при удалкнии несущ объкта не будет ошибки
print(a)

#compare

a1 = {2, 4,  6, 8, 'efe'}
a2 = {2, 4, 66, 8, 'eee', 'rr'}

print(a1.difference(a2))
print(a2.intersection(a1))
a1.intersection_update(a2) #delete all diff objects
a2.difference_update(a1)#delete all similiar obj




#dict

a = {}

#add
#1 
a.update(
    {
        1: '1', 
        2: ['ee', 'tt']
    }
)

print(a)

#2

a['hello'] = 'world'

print(a)

users = {
    "990908405567": {
        'name': 'Piter',
        'age': 15,
        'phone': '+ 7 777 000 88 00'
    },
    "990908407867": {
        'name': 'Stewe',
        'age':34,
        'phone': '+ 7 777 000 99 00'
    }
}

print(users.keys())
print(users.items())

from pprint import pprint

pprint(users)


print(users.get('990908405567'))

#remove

users.pop('990908405567')




'''
    PROBLEM 11:

Есть список Южноамериканских стран

Google Colab - 

СПИСОК №2

в котором Суринам встречается два раза. Необходимо написать программу,

которая удалит дублирующуюся запись, и возвратит в результате список.

'''


south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', \
  'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']

print(list(set(south_american_countries)))

# # Множество № 1:  
# # Множество № 2:
# farm_1 = {"dog", "cat", "mouse", "sheep"}
 
# # Множество № 3:
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
 
 
# # Словарь №1:
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
 
# a = input("Number a: ")
# symbol = input("What to do? ")
# b = input("Number b: ")
 
# if symbol == '+':
#   print(int(a) + int(b))


'''
PROBLEM 101:

Вы собираетесь на Иссык-Куль. Пока ваш чемодан пуст: 

suitcase = [] 

Однако он

может вместить всего 5 вещей.

Положите 5 вещей в чемодан.

Вы передумали, и решили убрать последнюю вещь. 
'''


suitecase = []

staff = ['Money', 'Shorts', 'Eyeglasses', 'Water', 'Passport']

suitecase.extend(staff)

suitecase.pop(-1)

print(suitecase)



'''
PROBLEM 27:

Создайте Dictionary с 5 элементами где ключи это их имена, а значение их профессия.

С помощь цикла for пройти вывести на экран строку:

"Здравствуйте <Имя>  Прекрасная профессия <Профессия>"

'''

people = {
    'Ork' : 'Doctor',
    'Piter' : 'Painter',
    'Olaf' : 'Taxidriver',
    'Anny' : 'Teacher',
    'Andy' : 'Programmer'
}

for k, v in people.items():
    print(f"Здравствуйте {k}!  Прекрасная профессия {v}")


'''
PROBLEM 0

Из множества 

№ 1 в Google Colab - удалите число 7.
'''
dates_of_birth = {3,10,11,7,31,21,1,10,3,5,6,6}
dates_of_birth.remove(7)
print(dates_of_birth)

'''

PROBLEM 1

Найти объекты которые есть и в SET №2 и в SET №3 из Google Colab 

PROBLEM 2

В SET №3 из Google Colab найдите объекты которых нет SET №2

'''


'''



PROBLEM 3

Создайте SET из 5 элементов. Потом добавьте в SET ещё один элемент.

А затем удалите через .pop() элемент и посмотрите что же вы удалили.
'''



#№1 Слияние словарей
# Напишите программу для слияния нескольких словарей в один.


my_friends = {
    "Joomart": "+77555246810",
    "Adinai": "+77555013579",
    "Ermek": "+77777013579",
    "Atai": "+77777246810",
    "Alymbek": "+77555501234",
}

his_her_friends = {
    "Lyazat": "+77551123456",
    "Salavat": "+77552234567",
    "Daniyar": "+77553345678",
    "Bolot": "+77554456789",
    "Alymbek": "+77555501234",
    "Dastan": "+77556678912",
    "Maksat": "+77557789012",
    "Adinai": "+77555013579",
}
our_friends = {} 


our_friends.update(his_her_friends)
our_friends.update(my_friends)

print(our_friends)

# №2 Покажите сколько у нас общих друзей
his_her_friends = {
    'Lyazat',
    'Salavat',
    'Daniyar',
    'Bolot',
    'Alymbek',
    'Dastan',
    'Maksat',
    'Adinai',
}

my_friends = {
    "Joomart",
    "Adinai",
    "Ermek",
    'Bolot',
    'Alymbek',
    'Dastan',
    "Atai",
    "Alymbek",
}

print(his_her_friends.intersection(my_friends))


'''№3 
Создайте переменное 
users= {}
Ключом у нас будет имена пользователей
Значение будет его пароль
И спросите у пользователя логин и пароль
Если такой логин уже есть 
   Скажите "Пользователь с таким логином уже существуюет"
Иначе добавьте как ключ и значение


В итоге покажите сколько у нас пользователей'''


users = {
    'user_1': {
        'login' : 'Vova',
        'password' : 'Qwerty123'
    },
    'user_2': {
        'login' : 'Yasha',
        'password' : 'Qwerty127'
    },
    'user_3': {
        'login' : 'Sonia',
        'password' : 'Qwerty125'
    }
}

login = input('Put ur login: ')
password = input('Put ur password: ')

logins = []
for i in users:
    logins.append(users[i]['login'])

if login not in logins:
    users.update(
        {f'user{3+1}': {
        'login' : login,
        'password' : password
    }})




