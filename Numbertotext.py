from telebot import TeleBot,types

TOKEN = "TEKEN"

bot = TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def command_start(message):
	bot.reply_to(message,"Salom botga xush kelibsiz,")
	
	
bot.polling()