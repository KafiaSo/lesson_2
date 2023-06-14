# Домашнее задание 
# 1. Пройдите в цикле по списку ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"] пока не встретие имя "Валера". 
# Когда найдете напишите "Валера нашелся". Подсказка: используйте метод list.pop() 
# 2. Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке
# 3. Написать функцию ask_user() чтобы помощью input() спрашивать пользователя "Как дела?", пока он не ответит "Хорошо"
# 4. При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет "Пока!" 

x = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"] 

import random
random_element = random.randint(0, len(x) - 1)
print(x[random_element])

def find_person(name):
    name = input("Кого ищем? ")

    while True:
        random_element = x.pop()
        if random_element == name:
            print(name, "?")
            print('{} нашелся'.format(name))
            break
        else:
            print(random_element, "?")
            print("Это не", name)

print(find_person("Валера"))

def ask_user():
    while True:
        user_say = input('Как дела? ').strip().lower()
        if user_say == 'хорошо':
            print('У меня тоже все хорошо')
  

def get_answer(): 
    while True:
        user_say = (input('Напиши мне что-нибудь: ')).lower()
        if user_say == 'Пока'.lower():
            print('Пока!')
            break
        else:
            print(get_answer(user_say))
            return(get_answer())
