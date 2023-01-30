#Program who play audio from an mp3 file
from playsound import playsound
playsound.init()
playsound.mixer.music.load('ex21.mp3')
playsound.mixer.music.play()
playsound.event.wait()