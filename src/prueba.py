import os

def listavoces():
    print('lista de voces disponibles:')
    scommand="espeak --voices=variant"
    os.system(scommand)

def leetexto(idioma, voz, texto):
    #idioma='es'; voz='m3'
    print('lectura de texto, idioma: "' + idioma + '", voz: ' + voz + ";")
    scommand='espeak -v' + idioma + '+' + voz +  ' --stdout ' + ' "' + texto + '"' + ' | aplay'
    print("$ " + scommand)
    os.system(scommand)

def textoaleer():
    print ("probaremos")
    rcomando='espeak --stdout -ves+m3 -p70 -s150 -k20 "Hola, estoy haciendo pruebas. Espero poder integarlo en Python" | aplay'
    os.system(rcomando)

listavoces()
leetexto('es','m3','Hola a todos. Lo siento, pero no hablo muy bien vuestro idioma')
#textoaleer()