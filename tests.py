# multi threading works
import threading
class test:
    def printer(self):
        for ctr in range(1000000):
            print("hello")

    def printHi(self):
        for ctr in range(1000000):
            print("hi")

if __name__ == "__main__":
    test1 = test()
    t1 = threading.Thread(target=test1.printHi)
    t2 = threading.Thread(target=test1.printer)
    t1.start()
    t2.start()
    print("Done!")

# speech recognition

import speech_recognition as sr


def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    with mic as source:
        audio = recognizer.listen(source, timeout=10)
        return recognizer.recognize_google(audio)
print(listen())