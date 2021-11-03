from selenium import webdriver
import speech_recognition as sr
import pyttsx3
import time

driver = webdriver.Chrome(executable_path='D:\\Programming\\python\\Projects\\Automation\\chromedriver_win32 (1)\\chromedriver.exe')
driver.get("https://web.whatsapp.com/")

listener = sr.Recognizer()
engine = pyttsx3.init() 


#users={
#	'friend':'any-name',
#}

def texttoSpeech(message):
	engine.say(message)
	engine.runAndWait()


def speechtoText():
	texttoSpeech("Press 1 for English and 2 for hindi")
	option=int(input("Enter 1.(English) 2.(Hindi): "))
	if (option==1):
	 	#with statement used for exception handling and more code clarity
		with sr.Microphone() as source:
			print('listening (in English)...')
			voice = listener.listen(source)

		try:
			info = listener.recognize_google(voice) 
			print(info)
			return info.lower()
		except:
			pass
	elif(option==2):
		#texttoSpeech("Till now its not available")
		with sr.Microphone() as source:
			print('listening (in hindi).....')
			voice = listener.listen(source)
		try:
			info = listener.recognize_google(voice,language='hi-IN')
			print(info)
			return info.lower()
		except:
			pass

def whatsp_auto(name,wp_message):
	time.sleep(1)
	texttoSpeech('Opening chat')
	time.sleep(1)
	user = driver.find_element_by_css_selector('span[title="{}"]'.format(name))
	user.click()
	time.sleep(1)
	texttoSpeech('Sending the message')
	time.sleep(1)
	mssg = driver.find_element_by_class_name('p3_M1')
	#send it by pressing the send button
	mssg.send_keys(wp_message)
	driver.find_element_by_class_name('_4sWnG').click()

def check_flag(flag):
	if(flag.lower()=='y'):
		#time.sleep(6)
		texttoSpeech("You pressed Y so lets jump in")
		time.sleep(1)
		texttoSpeech("Type the name in console to whom you want to send message : ")
		name=input("Enter the name : ")
		#reciever = users.get(name)
		#print(reciever)
		#time.sleep(1)
		#whatsp_auto(reciever)
		texttoSpeech('What you wanna type for the message?')
		wp_message = speechtoText()
		whatsp_auto(name,wp_message)
	elif(flag.lower()=='n'):
		texttoSpeech('Hey!Sad to hear Bye')
		print("Bye Bye :)")
		exit()
	elif(flag==''):
		texttoSpeech('You need to fill something in')
		flag_space=input("Enter a value (y/n):  ") 
		check_flag(flag_space)

def message_info():
	texttoSpeech("Hey there!Good Morning")
	texttoSpeech("Scan QR-Code")
	print('Scan QR Code')
	
	time.sleep(2)
	texttoSpeech('Waiting for your input buddy Type y or n in the console')

	flag=input("If done type yes or no (y/n):  ")
	check_flag(flag)


if __name__=='__main__':

	texttoSpeech('This code is donated by Mainak Das  Hope you will like it')
	texttoSpeech('Me myself a smart bot will guide you through this journey  Welcome')
	time.sleep(1)
	#calling this fun
	message_info()

	#whatsp_auto()
