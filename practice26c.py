from gtts import gTTS
tts = gTTS('i love you', lang='en')
tts.save('y.mp3')
print(">> File Created")