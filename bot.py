from pyowm import OWM
import os

owm = OWM('303d9ad9809c283d743c30ed87558ee4')
mgr = owm.weather_manager()

place = input ("В каком городе живете?: ")

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]

print("В городе " + place + " сейчас " + w.detailed_status)
print("Темп сейчас в районе " + str(temp))

if temp < 10:
	print( "Сейчас ппц как холодно, одевайся как танк!" )
elif temp < 20:
	print( "Сейчас холодно, оденься потеплее." )
else:
	print( "Температура норм, одевай что угодно." )

token - os.environ.get("BOT_TOKEN")