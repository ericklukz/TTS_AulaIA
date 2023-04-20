import pyttsx3
from datetime import datetime as dt

agora = dt.now()
hora = agora.hour
minuto = agora.minute

meses = {
    1 : "January",
    2 : "February",
    3 : "March",
    4 : "April"
}
dia = dt.today()
mes = dt.today().month
ano = dt.today().year

msg = "Now is " + str(hora) + "hours and" + str(minuto) + "minutes"
msg += "Today is" + str(dia) + "from" + meses[mes] + "from" + str(ano)

robo = pyttsx3.init()
robo.setProperty('rate', 120)#Taxa de palavras
robo.setProperty('volume', 1.0)#Volume da voz
robo.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
robo.say(msg)
robo.runAndWait()
