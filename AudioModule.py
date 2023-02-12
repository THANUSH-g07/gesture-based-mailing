import speech_recognition as sr
import pyttsx3
import threading


class ThunderAssistant:
    @staticmethod
    def speak(message):
        engine = pyttsx3.init()
        engine.say(message)
        engine.runAndWait()

    @staticmethod
    def listen():
        r = sr.Recognizer()
        mic = sr.Microphone(device_index=1)
        with mic as source:
            print("listening ...")
            audio = r.listen(source, timeout=10)
            text = r.recognize_google(audio)
            return text


if __name__ == "__main__":
    print(ThunderAssistant.listen())
    print("Done!")
