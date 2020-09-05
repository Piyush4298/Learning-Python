from gtts import gTTS
import os

f = open('text_file.txt')
x = f.read()
language = 'en'
audio = gTTS(text=x, lang=language, slow=False)
audio.save('text_to_speech.wav')
os.system('text_to_speech.wv')
