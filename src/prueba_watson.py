#from tts_watson.TtsWatson import TtsWatson
#import time

#voice = TtsWatson("carlycharly@hotmail.com","3pj58q.L", "es-ES_LauraVoice")
#print("credenciales generadas")
#time.sleep(5)
#voice.play("Hola mundooooo")
from watson_text_talker import *

text_talker = TextTalker('BjHfv8ct-Rypjy23mYp8q1pF74kHBEEwa0JBkP4tR2ne', 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/d383fac8-02d5-4896-b8d0-373e50273e1c')

text_talker.say("Hello world!")
