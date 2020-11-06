from pyowm import OWM
import os

owm = OWM('303d9ad9809c283d743c30ed87558ee4')
mgr = owm.weather_manager()
#bot = telebot.TeleBot("1418329273:AAF3ppRF116NV6RaSxVUdrBJJH97vzhpBpA")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = mgr.weather_at_place( message.text )
	w = observation.weather
	temp = w.temperature('celsius')["temp"]

	answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
	answer += "Температура сейчас в районе " + str(temp) + "\n\n"

	if temp < 10:
		answer += "Сейчас ппц как холодно, одевайся как танк!"
	elif temp < 20:
		answer += "Сейчас холодно, оденься потеплее."
	else:
		answer += "Температура норм, одевай что угодно."

	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )

token - os.environ.get("BOT_TOKEN")

bot.run(str(token))
