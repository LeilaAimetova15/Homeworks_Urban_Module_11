# 1. Библиотека Requests
import requests

# Отправление GET-запроса на API:
r = requests.get('https://pypi.org')

# Чтение ответов
#print(r.text)

# Использование заголовков запросов
print(r.headers)           #информация о сервере, дата, кодировка и т.д.
print(r.headers['Date'])   #вывод даты, хранящуюся в заголовке ответа

# Отправление POST-запроса:
r = requests.post('https://pypi.org', data={'key': 'value'})
print(r.text)

#Отправка данных с помощью аутентифицированных запросов
#отправка POST-запроса с полезной нагрузкой в формате JSON и базовой аутентификацией
url = 'https://api.github.com'
payload = {'key1': 'value1', 'key2': 'value2'}
auth = ('username', 'password')
headers = {'Content-Type': 'application/json'}
r = requests.post(url, json=payload, auth=auth, headers=headers)
if r.status_code == 200:
    print('Данные отправлены успешно')
else:
    print('Ошибка при отправке данных:', r.text)

# 2. Библиотека NumPy
import numpy as np

#Создание массива
massiv1 = np.array([12, 13, 14, 15, 16]) #можно передать как кортеж (12, 13, 14, 15, 16)
print(massiv1)

#Трехмерный массив с определением размерности массива
massiv3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(massiv3)
print(massiv3.ndim)

#Итерация по массивам с помощью цикла for
massiv_iter = np.array([10, 12, 13, 14, 15])
for i in massiv_iter:
    print(i)

#Преобразование из одномерного в двумерный массив
massiv_2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_massiv = massiv_2.reshape(3, 4)
print(new_massiv)

#Определение дисперсии - т.е. на сколько данные отличаются друг от друга и от среднего значения.
m = np.array([[20, 21, 22], [23, 24, 25]])
var_all = m.var()         #Дисперсия всех элементов массива
print(var_all)
var_axis0 = m.var(axis=0) #Дисперсия элементов вдоль оси 0
print(var_axis0)
var_axis1 = m.var(axis=1) #Дисперсия элементов вдоль оси 1
print(var_axis1)

# 3. Библиотека Pillow
from PIL import Image

# Открытие файла, а также изображения на экране
im = Image.open('red_cat.jpg')
im.show()

# Получение данных о файле:
print(im.format, im.size, im.mode)

# Изменение размера изображения и вывод на экран обновленного изображения:
new_image = im.resize((368, 530))
im.show()

# Применение эффекта размытия
r, g, b = new_image.split()
new_image = Image.merge("RGB", (b, g, r))

# Конвертирование изображения в другой формат и сохранение
new_image.save('red_cat.png', format='PNG')
