import speech_recognition
import pyttsx3
import sys

def talk(words):
	engine = pyttsx3.init()
	engine.say(words)
	engine.runAndWait()

talk('Слушаю')

def command():
	r = sr.Recognizer()

	with sr.Microphone(device_index = 1)as source:
		audio = r.listen(source)

	try:
		task - r.recognize_google(audio, language = 'ru-RU').lower()
		print(f'[log] Уловил: {task}')
	except:
		talk('Я вас не расслышал, повторите')
		task = command()
	return task 

def working(task):
	if 'привет' in task:
		talk('Здравствуйте!')
	elif 'стоп' in task:
		talk('Ухожу на покой')
		sys.exit()

while True:
	working(command())