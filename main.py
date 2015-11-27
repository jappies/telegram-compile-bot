import telebot
import requests
import csv

bot = telebot.TeleBot('128376654:AAEOiL_whbfpLhc2_t2s6NoQGnW6141YqNU')

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    welcome_string = """This bot can compile code given to it, using pastebin
    urls. Just use /compile <language> <pastebin_id>
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

    input_file = csv.DictReader(open("languages.csv"))

    id = -1

    for row in input_file:
        if row["name"] == arguments[1]:
            id = row["id"]

    if id is -1:
        bot.reply_to(message,  "Language is not supported")
        return

    code = requests.get('http://pastebin.com/raw.php?i=' + arguments[0])
    if code.status_code != 200 or "Page Is Removed" in code:
        bot.reply_to(message, "Error while getting code")
        return;
    print "test"

    args = {}
    args["language"] = id
    args["code"] = code
    args["stdin"] = "#banmartijn"
    r = requests.post("http://carlosvanrooijen.nl:8082/compile", data = args,
                        timeout=10)

    output = r.json()

    print output
    response = "Output: \n"
    if output["errors"]:
        response += "An error occured: \n"
        response += output["errors"]
        bot.reply_to(message, response)
        return

    response += output["output"][0:200] + "\n etc. \n"
    response += "Execution time: " + output["time"][:-2] + " seconds\n"
    response += "URL: https://pastebin.com/raw.php?i=" + arguments[0] + "\n"
    bot.reply_to(message, response)


@bot.message_handler(commands=['languages'])
def print_languages(message):
    input_file = csv.DictReader(open("languages.csv"))
    response = "Supported languages:\n"
    for row in input_file:
        response += row["name"]
        response += "\n"

    bot.reply_to(message,response)

if __name__ == "__main__":
    bot.polling()
