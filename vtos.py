# Import the required module for text 
# to speech conversion
from gtts import gTTS
import pygame 
# This module is imported so that we can 
# play the converted audio
import os
import time
# The text that you want to convert to audio
mytext = "A prosthetic hand with 8 degrees of freedom available at less cost in market"
 
# Language in which you want to convert
language = 'en'
 
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
 
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
 
# Playing the converted file
#os.system("welcome.mp3")
#music = pyglet.resource.media('welcome.mp3')
#music.play()

#pyglet.app.run()
pygame.init()

pygame.mixer.music.load("welcome.mp3")

pygame.mixer.music.play()

time.sleep(10)
