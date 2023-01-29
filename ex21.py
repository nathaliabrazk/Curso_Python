#Program who play audio from an mp3 file
import pyaudio
pyaudio.init()
pyaudio.mixer.music.load('ex21.mp3')
pyaudio.mixer.music.play()
pyaudio.event.wait()