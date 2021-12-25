import speech_recognition as sr
import pyttsx3
import threading

class ThunderAssistant:

    def speak(self, message):
        engine = pyttsx3.init()
        engine.say(message)
        engine.runAndWait()

    def printer(self):
        for ctr in range(1000000):
            print("hello")

    def printHi(self):
        for ctr in range(1000000):
            print("hi")

    def listen(self):
        r = sr.Recognizer()
        mic = sr.Microphone(device_index=1)
        with mic as source:
            audio = r.listen(source, timeout=10)
            return r.recognize_google(audio)

if __name__ == "__main__":
    assitant = ThunderAssistant()
    assitant.listen()
    #t1 = threading.Thread(target=assitant.speak("hello"))
    #t2 = threading.Thread(target=assitant.listen())
    #t1.start()
    #t2.start()
    print("Done!")