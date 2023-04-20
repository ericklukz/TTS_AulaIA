from gtts import gTTS
from pygame import mixer

audio = gTTS("agora acreditas no malusco?", lang='pt')
audio.save("malusco.mp3")

mixer.init()
mixer.music.load("malusco.mp3")
mixer.music.play()
input("Digite qualquer coisa para finalizar")
