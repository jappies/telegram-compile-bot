import telebot

bot = telebot.TeleBot('128376654:AAEOiL_whbfpLhc2_t2s6NoQGnW6141YqNU')

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    welcome_string = """This bot can compile code given to it, using pastebin
    urls. Just use /compile <language> <pastebin_url>
    to start! Use /languages to print a list
    of all supported languages in a table!
    Happy compiling ^^"""

    bot.reply_to(message, welcome_string)

@bot.message_handler(commands=['compile'])
def compile_link(message):
    arguments = message.text.split(" ")
    if len(arguments) < 3:
        bot.reply_to(message, "Not enough arguments :c")
        return
    arguments = arguments[1:]
    bot.reply_to(message, "Compiling...")


if __name__ == "__main__":
    bot.polling()
