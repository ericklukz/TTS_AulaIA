from gtts import gTTS
import os

audio = gTTS("agora acreditas no malusco?", lang='pt')
audio.save("malusco.mp3")
os.system("malusco.mp3")

input("Digite qualquer coisa para finalizar")
