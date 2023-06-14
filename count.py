from collections import Counter

phones = ["iPhone", "Samsung", "LG", "IPhone", "Iphone", "LG"]

count = Counter(phones)
print(count)



from collections import Counter

phones = ["iPhone", "Samsung", "LG", "IPhone", "Iphone", "LG"]

count = Counter(phones)
print(count["Hello"])

text = "Ехал Грека через реку видит Грека в реке рак"
count = Counter(text)
print(count)



import ephem

mars = ephem.Mars('2000/01/01')
print(mars)



import ephem

mars = ephem.Mars('2000/01/01')
const = ephem.consellation(mars)

print(const)


# Установите модуль ephem
# Добавьте в бота команду /planet, 
# которая будет принимать на вход название планеты на английском, 
# например /planet Mars
# В функции-обработчике команды из update.message.text 
# получите название планеты (подсказка: используйте .split())
# При помощи условного оператора if и ephem.constellation 
# научите бота отвечать, в каком созвездии сегодня находится планета.

import ephem

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
    
    if  user_text:
        planet_name = update.message.text 

        try:
            planet = detali(ephem, planet_name)
            ephem_answer = ephem.constellation(planet)
            logging.ephem(planet_name)
            update.message.reply_text(user_text[1])
        except AttributeError:
             update.message.reply_text("I don't know {} planet.".format(planet_name,) + '\n' + GREETING)

        user_data['asked'] = False
    else:
        update.message.reply_text(GREETING)

def astronomy(bot, update, user_data):
    text = 'What planet are you interested in?'
    user_data['asked'] = True
    update.message.reply_text(text)

def main():
    mybot = Updater("6288351373:AAE9nTQUv-uKYq_3SNiHACQNSTH-u4ipZXw", use_context = True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

main()












