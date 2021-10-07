import speech_recognition as sr
import pyttsx3
r=sr.Recognizer()
eng = pyttsx3.init()

def recorder():
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        voice_in=''
        try:
            voice_in=r.recognize_google(audio)
            print("You:",voice_in)
        except sr.UnknownValueError:
            print("Sorry, I did not get that.")
            eng.say("Sorry, I did not get that.")
            eng.runAndWait()
        except sr.WaitTimeoutError:
            print("Wait timeout error.")
            eng.say("Wait timeout error.")
            eng.runAndWait()
        except sr.RequestError:
            print("Sorry, the service is currently down.")
            eng.say("Sorry, the service is currently down.")
            eng.runAndWait()
        return voice_in
