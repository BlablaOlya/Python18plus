import telebot

token = '1094854833:AAHiNW-N9Gj-VuLCdinKM8b6v7opU2hPYm0'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["start"])

def repeat_all_messages(message):
    bot.send_message(message.chat.id, "Добро пожаловать! ")



@bot.message_handler(content_types=['text'])
def repeat_joke_messages(message):
    if message.text.lower() == 'Саня':
        bot.send_message(message.chat.id, 'Саня открой дверь! Сань, ну пусти... Холодно же')
    elif message.text.lower() == 'Пока':
        bot.send_message(message.chat.id, 'До встречи!')


bot.infinity_polling()