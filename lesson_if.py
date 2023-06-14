balance = 100
price = 50
in_stock = 10

print(bool(balance > price))
print(bool(in_stock))

if balance > price and in_stock:
    print('Одобряем оплату покупки')
else:
    print('Пожалуйста, пополните баланс!')


def check_weather(temperature):
    if temperature < 0:
        return "На улице холодно"
    elif temperature >= 0 and temperature < 15:
        return "На улице прохладно"
    elif temperature >= 15 and temperature < 2:
        return "На улице тепло"
    else:
        return "На улице жарко"
    
print(check_weather(-10)) #На улице холодно
print(check_weather(8)) #На улице прохладно
print(check_weather(20)) #На улице тепло
print(check_weather(30)) #На улице жарко


classes = [
    {'name': '3А', 'scores' : [3, 4, 4, 5, 2]},
    {'name': '3Б', 'scores' : [5, 5, 3, 2, 2]},
    {'name': '3В', 'scores' : [4, 5, 3, 5, 4]},
]

def count_class_avg(student_scores):
    scores_sum = 0
    for score in student_scores:
        scores_sum += score
    return scores_sum / len(student_scores)

school_avg_sum = 0
for one_class in classes:
    class_avg = count_class_avg(one_class['scores'])
    print(f'Средняя оценка класса {one_class['name']}: {class_avg}')
    school_avg_sum += class_avg

school_avg = round(school_avg_sum / len(classes), 2)
print(f'Средняя оценка по школе: {school_avg})
