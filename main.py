from yandexgpt import talk_to_yandex_gpt
import telebot

bot=telebot.TeleBot('7671695418:AAHLiu5gDE_U-xojl2agyBmaRuQUbLO6yzw')

# 7671695418:AAHLiu5gDE_U-xojl2agyBmaRuQUbLO6yzw
@bot.message_handler(commands = ['start'])
def start(message):
    print(message)
    bot.send_message(message.chat.id, 'Здраствуйте! Ваш Асистент. Чем могу помочь?')

@bot.message_handler(func= lambda message: True)
def handle_message(message):
    print(message.text)
    bot.send_message(message.chat.id, talk_to_yandex_gpt([{"role": "user", "text": message.text}])) 

bot.polling()


#/print ('Здраствуйте! Ваш Асистент. Чем могу помочь?')
#dialog = []
#   "role": "user",
 #   "text": input('Вы: ')
#  }
 # if user_message['text']=='/reset':
#    dialog = []
#  else:
 #  dialog.append(user_message)
 #  assistent_message = {
  #    "role": "assistent",
  #    "text": talk_to_yandex_gpt(dialog),
  #  }
  # dialog.append(assistent_message)
  # print(assistent_message ['text'])
      