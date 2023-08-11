# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке.

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  


stroka1 = 'пара-ра-рам рам-пам-папам па-ра-па-да'
# stroka1 = input("Введите строку: ")
stroka2 = stroka1.split()
stroka3 = []
glasn = 'ауеыоэяиюё'
for word in stroka2:
    result1 = 0
    for i in word:
        if i in glasn:
            result1 += 1
    stroka3.append(result1)
print(stroka3)
if len(set(stroka3)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')
