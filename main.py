#main
import record
import moduleswitcher as ms
import pyttsx3
eng = pyttsx3.init()
print("Welcome to Voice Coding!")
eng.say("Welcome to Voice Coding!")
eng.runAndWait()
print("Speak something to write your code")
eng.say("Speak to write your code")
eng.runAndWait()
# flag=1
# while flag==1:
#     eng.say("Entering Module Shifter")
#     eng.runAndWait()
#     voice_in=record.recorder()
#     flag=ms.shifter(voice_in)