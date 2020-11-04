#from tts_watson.TtsWatson import TtsWatson
#import time

#voice = TtsWatson("carlycharly@hotmail.com","3pj58q.L", "es-ES_LauraVoice")
#print("credenciales generadas")
#time.sleep(5)
#voice.play("Hola mundooooo")
from watson_text_talker import *

text_talker = TextTalker(username='carlycharly@hotmail.com', password='3pj58q.L')

text_talker.say("Hello world!")
