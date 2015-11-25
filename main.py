import telebot

bot = telebot.TeleBot('128376654:AAEOiL_whbfpLhc2_t2s6NoQGnW6141YqNU')

@bot.message_handler(commands=['start', 'help'])
def hi(message):
    bot.reply_to(message, "ey :D")

if __name__ == "__main__":

    bot.polling()
