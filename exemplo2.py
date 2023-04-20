import pyttsx3

robo = pyttsx3.init()
robo.setProperty('rate', 140)#Taxa de palavras
robo.setProperty('volume', 1.0)#Volume da voz

msg = 'hello world'
vozes = robo.getProperty('voices')

for voz in vozes:
    print(voz.id)
    robo.setProperty('voice', voz.id)
    robo.say(msg)
    robo.runAndWait()
