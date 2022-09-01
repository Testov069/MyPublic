import telebot
from config import token, keys
from extensions import ExchangeException, Exchange

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = 'Это Бот-Конвертер валют и вот, что я умею:  \n- Показывать список доступных валют для конвертации через команду /values \
    \n- Выводить конвертацию валюты через команду <имя валюты для конвертации> <в какую валюту конвертировать> <количество конвертируемой валюты>\n \
- Узнать, что я могу через команду /help'
    bot.reply_to(message, text)


@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать конвертацию валют, введи команду боту в следующем формате: \n<имя валюты для конвертации> <в какую валюту конвертировать> <количество конвертируемой валюты>\nУзнать список всех доступных валют для конвертации, введи команду\n/values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ExchangeException('Ошибка в количестве параметров')

        quote, base, amount = values
        total_base = Exchange.get_price(quote, base, amount)
    except ExchangeException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Что-то пошло не так с {e}')
    else:
        text = f'Перевожу {quote} в {base}\n{amount} {quote} = {total_base} {base}'
        bot.send_message(message.chat.id, text)


bot.polling()
