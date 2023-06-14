for number in range(3):
    print(f'Номер {number}')

for letter in 'python':
    print(letter.upper())

my_string = 'Привет я учу python'

for word in my_string.split():
    print(f'Длина слова {word}: {len(word)}')

student_scores = [3, 5, 4, 4, 2]

avg_score = 0
for score in students_scores:
    print('До', avg_score)
    avg_score = avg_score + score
    print('После', avg_score)



student_scores = [3, 5, 4, 4, 2]

avg_score = 0
for score in students_scores:
    avg_score = avg_score + score
    
class_avg = avg_score / len(students_scores)
print(class_avg)


stock = [
    {'name': 'iPhone 12', 'stock': 24, 'price': 65432.1,
     'discount': 25},
    {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.0,
     'discount': 10},
    {'name': '', 'stock': 18, 'price': 10000.0, 'discount': 10},
]

def discounted(price, discount, max_discount=30, phone_name = ''):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError("Слишком большая максимальная скидка")
    if discount >= max_discount:
        return price
    elif 'iphone' in phone_name.lower() or not phone_name:
        return price
    else:
        return price - (price * discount / 100)

for phone in stock:
    phone['price_final'] = discounted(phone['price'], phone ['discount'], phone_name = phone['name'])

print(stock)