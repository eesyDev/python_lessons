#1

str_1 = input('Put some word....: ')
str_2 = input('Put some word....: ')
str_3 = input('Put some word....: ')

list_full =[]

list_full.append(str_1)
list_full.append(str_2)
list_full.append(str_3)

if str_1.isalpha() and len(str_1) > 20 and str_2.isalpha() and len(str_2) and str_3.isalpha() and len(str_3):
    print(max(list_full, key = len))
    list_full.remove(max(list_full, key = len))
    print(list_full)



#2

mail_input = input('Put ur email: ')

mail_splited = mail_input.split('@')
print(mail_splited)
if mail_input.endswith('gmail.com')  or mail_input.endswith('mail.ru'): 
    num = int(input('Put num 666999: '))
    if num == 666999:
        print('Success')
    else: 
        print('Error')
    print('Your e-mail is incorrect')
else:
    print('Your e-mail is incorrect')


#3

digit_1 = 2897607

if digit_1 % 3 == 0:
    res = (digit_1 // 3) ** 2
    str_to = str(res)
    print(len(str_to))


#9

yoda = ['on Python', 'programming ', 'I like ']

print(f'{yoda[2]} {yoda[1]} {yoda[0]}')



#12

# № 12
# У нас есть wather_dict
# тут хранятся все данные о сегоднешней погоде
# Вам необходимо его расспоковать 
# тоесть взять данные и записать как показано ниже

# вывода на экран:
# Дата: 2022-10-26
# Время: 11:33
# Погода в городе: Almaty 
# Температура:  9.18 °C  
# Описание: moderate rain
# Облачность: 100
# Влажность: 71
# Давление: 1022  мм.рт.ст
# Скорость ветра: 4.99

wather_dict = {'base': 'stations',
 'clouds': {'all': 100},
 'datetime': '2022-10-26 11:33:21.774524',
 'main': {'feels_like': 6.57,
          'grnd_level': 925,
          'humidity': 71,
          'pressure': 1022,
          'sea_level': 1022,
          'temp': 9.18,
          'temp_max': 9.18,
          'temp_min': 9.18},
 'name': 'Almaty',
 'rain': {'1h': 1.26},
 'sys': {'country': 'KZ', 'sunrise': 1666747131, 'sunset': 1666785198},
 'timezone': 21600,
 'visibility': 10000,
 'weather': [{'description': 'moderate rain',
              'icon': '10d',
              'id': 501,
              'main': 'Rain'}],
 'wind': {'deg': 262, 'gust': 9.09, 'speed': 4.99}}

date_time_sp = (wather_dict.get('datetime').split())
time_sp = date_time_sp[1].split('.')
main_sp = wather_dict.get('main')
descr = wather_dict.get('weather')


description = descr[0].get('description')
clouds = wather_dict.get('clouds').get('all')
humidity = main_sp.get('humidity')
pressure = main_sp.get('pressure')
date = date_time_sp[0]
time = time_sp[0]
city = wather_dict.get('name')
temp = main_sp.get('temp')
wind_speed = wather_dict.get('wind').get('speed')


print(
f'''
Дата: {date}
Время: {time}
Погода в городе: {city} 
Температура: {temp}
Описание: {description}
Облачность: {clouds}
Влажность: {humidity}
Давление: {pressure}
Скорость ветра: {wind_speed}

'''
)

