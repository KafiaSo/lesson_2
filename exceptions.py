def cut_cake(people):
    parts = 1 / people
    print(f'Каждый человек получит {parts} пирога')

cut_cake(0)


def cut_cake(people):
    try:
        parts = 1 / people
        print(f'Каждый человек получит {parts} пирога')
    except ZeroDivisionError: на: str
    print('Не надо делить на ноль!')
    
cut_cake(0)


def cut_cake(people):
    try:
        parts = 1 / people
        print(f'Каждый человек получит {parts} пирога')
    except ArithmeticError:
        print('Не надо делить на ноль!')
    except TypeError:
        print('Программа принимает число') 
    
cut_cake(0)


# Перепишите функцию hello_user() из задания про while, 
# чтобы она перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
# и завершала работу при помощи оператора break

while True:
    hello_user = input('Ты уже уходишь? ')
    try: 
        hello_user == 'Пока'
    except KeyboardInterrupt:
        print('Пока!') 
        break


# Перепишите функцию discounted(price, discount, max_discount=20) из урока про функции так, 
# чтобы она перехватывала исключения, когда переданы некорректные аргументы.
# Первые два нужно приводить к вещественному числу при помощи float(), 
# а третий - к целому при помощи int() и перехватывать исключения ValueError и TypeError, 
# если приведение типов не сработало.

def discounted(price, discount, max_discount=20):
    try:
        if(not type(price) is int or not type(discount) is int or not type(max_discount) is int):
            raise TypeError('Должно быть приближено к числу')
        else:
            price = abs(price)
            discount = abs(discount)
            max_discount = abs(max_discount)
            if max_discount >= 100:
                raise ValueError("Слишком большая максимальная скидка")
            if discount >= max_discount:
                return price
            else:
                return price - (price * discount / 100)

    except TypeError as not_int:
        print(not_int)
    except ValueError as big_discount:
        print(big_discount)