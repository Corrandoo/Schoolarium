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

def handle_message_with_numbers(message):
    arguments = message.getText.split(" ")
def polling():
    bot.polling(none_stop=True)

if __name__ == '__main__':
    thread1 = Thread(target=polling)
    thread1.start()