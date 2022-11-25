import telebot
from telebot import types
import requests
from random import randint

api_token = '5789431042:AAGM5OLPk44Xfk5izNuVWaiPxPVISLawMwY'

bot = telebot.TeleBot(api_token)


# duck_phrases = ['Remember, you can take an unlimited number of ducks...', 'Take one more duck.',
                # 'There are not enough ducks. Press the button again.']


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_td = types.KeyboardButton('take a duck')
    button_ed = types.KeyboardButton('enough ducks')
    markup.add(button_td, button_ed)
    bot.send_message(
        message.chat.id,
        text='Hey, {0.first_name}! I have something for you...\nPress the button below ;)'.format(
            message.from_user),
        reply_markup=markup
    )


@bot.message_handler(content_types=['text'])
def give_a_duck(message):
    if (message.text == 'take a duck'):
        # rand_num = randint(0,3)
        bot.send_message(message.chat.id, text='*the duck is loading*')
        response = requests.get(f'https://random-d.uk/api/random')
        a = response.json()
        img = requests.get(a['url'])
        with open('new_image.jpg', 'wb') as f:
            f.write(img.content)
        ph = open('new_image.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=ph)
        # bot.send_message(message.chat.id, text=duck_phrases[rand_num])
    elif (message.text == 'enough ducks'):
        bot.send_message(
            message.chat.id, text="Fine, I'll be waiting for you until you miss pictures with ducks again!")
    else:
        bot.send_message(
            message.chat.id,
            text="Sorry, I don't know what that means.\nMaybe you still want to take a duck?")


bot.polling(none_stop=True)
