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
### Mathematics section
@bot.message_handler(regexp='Математика')
def handle_math_message(message):
    markup = types.ReplyKeyboardMarkup()
    sqr_equalition = types.KeyboardButton('Квадратные уравнения')
    markup.add(sqr_equalition)
    bot.send_message(message.chat.id, "Вы вошли в математический режим. "
                                             "Выберите опцию, с которой хотите работать.", reply_markup=markup)

@bot.message_handler(regexp='Квадратные уравнения')
def handle_equalition_message(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    sent = bot.send_message(message.chat.id,
                            "Я могу посчитать корни квадратного уравнения. Введите коэффициенты a, b и c через пробел."
                            "Не забывайте про знаки! Если число отрицательное, то ставится -(тире)."
                            "Если число положительное, то ничего не ставится.", reply_markup=markup)
    bot.register_next_step_handler(sent, handle_message_with_numbers)
def handle_calculator_message(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    sent = bot.send_message(message.chat.id, "Вы вошли в опцию калькулятора. "
                                             "Умножение: *, деление: /, квадратный корень: s(извлекаемое выражние).",
                            reply_markup=markup)
    bot.register_next_step_handler(sent, handle_message_with_calculate_numbers)
def handle_message_with_calculate_numbers(message):
    s_argument = message.text.split
    result = logic.calculate(s_argument)
    if result == False:
        sent = bot.send_message(message.chat.id, "Запрос не выполнен из-за сильной потенциальной нагрузки.")
        bot.register_next_step_handler(sent, handle_message_with_calculate_numbers)
        return
    bot.send_message(message.chat.id, str(result))

def handle_message_with_numbers(message):
    try:
        arguments = message.text.split(" ")
        bot.send_message(message.chat.id, logic.count_equality(float(arguments[0]), float(arguments[1]), float(arguments[2])))
    except:
        sent = bot.send_message(message.chat.id, "Возникла ошибка. Проверьте введенные данные и повторите ввод еще раз.")
        bot.register_next_step_handler(sent, handle_message_with_numbers)

def polling():
    bot.polling(none_stop=True)

if __name__ == '__main__':
    thread1 = Thread(target=polling)
    thread1.start()