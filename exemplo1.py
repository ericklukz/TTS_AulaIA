import pyttsx3

robo = pyttsx3.init()
robo.setProperty('rate', 150,)#Taxa de palavras
robo.setProperty('volume', 1.0)#Volume da voz

msg = "masqueico"

robo.say(msg)
robo.runAndWait()
