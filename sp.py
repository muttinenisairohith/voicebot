#Python 2.x program to transcribe an Audio file
while(1):	
	import speech_recognition as sr

	import pyaudio
	import wave
	import sys

	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	RECORD_SECONDS = 3
	WAVE_OUTPUT_FILENAME = "abc.wav"

	if sys.platform == 'darwin':
	    CHANNELS = 1

	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,
		        channels=CHANNELS,
		        rate=RATE,
		        input=True,
		        frames_per_buffer=CHUNK)

	print("* recording")

	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	    data = stream.read(CHUNK)
	    frames.append(data)

	print("* done recording")

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()



	 
	AUDIO_FILE = ("abc.wav")
	 
	# use the audio file as the audio source
	 
	r = sr.Recognizer()
	 
	with sr.AudioFile(AUDIO_FILE) as source:
	    #reads the audio file. Here we use record instead of
	    #listen
	    audio = r.record(source)  
	 
	try:
	    mytext = r.recognize_google(audio)
	    print("The audio file contains: " + r.recognize_google(audio))
	 
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	 
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))

	mytext1=mytext
	import csv
	import difflib
	file = open('dbc.csv',"rb")
	reader = csv.reader(file)
	for row in reader:
		if (mytext ==row[0]):
			mytext = row[1]
			print mytext
			break
		else:
			score = difflib.SequenceMatcher(None,mytext.lower(),row[0].lower()).ratio()
			if score>=0.85:
				mytext =row[1]
				break
	from gtts import gTTS
	import pygame 
	# This module is imported so that we can 
	# play the converted audio
	import os
	import time
	# The text that you want to convert to audio
	#mytext = 'Welcome to geeksforgeeks!'
	 

	language = 'en'
	 

	myobj = gTTS(text=mytext, lang=language, slow=False)
	 

	myobj.save("welcome.mp3")
	 
	# Playing the converted file
	#os.system("welcome.mp3")
	#music = pyglet.resource.media('welcome.mp3')
	#music.play()

	#pyglet.app.run()
	pygame.init()

	pygame.mixer.music.load("welcome.mp3")

	pygame.mixer.music.play()

	time.sleep(2)

