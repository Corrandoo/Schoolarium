from threading import Thread
from telebot import types
import telebot, config, logic

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def handle_first_command(message):
    bot.send_message(message.chat.id, "Добрый день! Управление ботом очень простое: просто выберите нужную Вам опцию и нажмите на нее.")
    markup = types.ReplyKeyboardMarkup()
    math = types.KeyboardButton('Математика')
    markup.add(math)
    bot.send_message(message.chat.id, "Выберите режим бота:", reply_markup=markup)

@bot.message_handler(regexp='Математика')
def handle_math_message(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    sent = bot.send_message(message.chat.id, "Я могу посчитать корни квадратного уравнения. Введите коэффициенты a, b и c через пробел."
                                      "Не забывайте про знаки! Если число отрицательное, то ставится -(тире)."
                                      "Если число положительное, то ничего не ставится.", reply_markup=markup)
    bot.register_next_step_handler(sent, handle_message_with_numbers)

def handle_message_with_numbers(message):
    try:
        arguments = message.text.split(" ")
        bot.send_message(message.chat.id, logic.count_equality(float(arguments[0]), float(arguments[1]), float(arguments[2])))
    except:
        pass

def polling():
    bot.polling(none_stop=True)

if __name__ == '__main__':
    thread1 = Thread(target=polling)
    thread1.start()