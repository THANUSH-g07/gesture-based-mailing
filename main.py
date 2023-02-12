import cv2
import time
import HandTrackingModule as htm
import speech_recognition as sr
import pyttsx3
import smtplib
from MailModule import ThunderMail as tm
from AudioModule import ThunderAssistant as ta

email = "harsha6286@gmail.com"
password = "nezohxjckmydnlyx"

def comlete_string(S):
    total = ""
    S_li = list(S.split())
    for i in S_li:
        if i.strip() == "at":
            total += "@"
        elif i.strip() == "vi":
            total += "6"
        else:
            total += i.strip()
    return total.lower()


print("debug")

# ta.speak("Hello this is Thunder Assistant.")
# ta.speak("Use L for login.")
# ta.speak("Victory for sending mail")
# ta.speak("Swag for reading mail")
# ta.speak("stop for exit")


def listen():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    with mic as source:
        global email
        global password
        global mail_to
        print("Speech Activated")
        ta.speak("Tell your Mail id")
        audio = r.listen(source, timeout=10)
        email = r.recognize_google(audio)
        email = comlete_string(email)
        print(f'email is:\n{email}')
        ta.speak("Tell your Password")
        audio = r.listen(source, timeout=10)
        password = r.recognize_google(audio)
        password = comlete_string(password)
        print(f'password is:\n{password}')


wCam, hCam = 800, 900

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
over_image = cv2.imread("cetlogo.jpg")
print(over_image.shape)
# overlayList = [over_image]
detector = htm.HandDetector(detectionCon=0.75)


def HandGesture():
    pTime = 0
    # finger_open = 0
    tipIds = [i for i in range(4, 21, 4)]
    zero_acc = [0] * 5
    Accuracy_factor = 35
    while True:
        Accurate_ctr1, Accurate_ctr2, Accurate_ctr3, Accurate_ctr4, Accurate_ctr5 = zero_acc[0], zero_acc[1], zero_acc[
            2], \
                                                                                    zero_acc[3], zero_acc[4]
        ret, img = cap.read()
        img = detector.findHands(img)
        lmlist = detector.findPosition(img, draw=False)
        if len(lmlist) > 0:
            fingers = []
            # Thumb
            if lmlist[tipIds[0]][1] > lmlist[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            # Remaining fingures
            for id in range(1, 5):
                if lmlist[tipIds[id]][2] < lmlist[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            # print(fingers)
            # Thumbs up
            if fingers[0] == 1 and sum(fingers) == 1:
                zero_acc[0] += 1
                if Accurate_ctr1 > Accuracy_factor:
                    print("thums up")
                    zero_acc = [0] * 5
            if fingers[0] == 1 and fingers[1] == 1 and sum(fingers) == 2:
                zero_acc[1] += 1
                if Accurate_ctr2 > Accuracy_factor:
                    listen()
                    zero_acc = [0] * 5
            # Swag
            if fingers[1] == 1 and fingers[4] == 1 and fingers[0] == 1 and sum(fingers) == 3:
                zero_acc[2] += 1
                if Accurate_ctr3 > Accuracy_factor:
                    em = email.strip()
                    passw = password.strip()
                    tm.read_mail(em, passw)
                    zero_acc = [0] * 5
            # victory
            if fingers[1] == 1 and fingers[2] == 1 and sum(fingers) == 2:
                zero_acc[3] += 1
                if Accurate_ctr4 > Accuracy_factor:
                    r = sr.Recognizer()
                    mic = sr.Microphone(device_index=1)
                    with mic as source:
                        global to_add
                        global mail_body
                        ta.speak("To Whom you want to send the mail")
                        audio = r.listen(source, timeout=10)
                        to_add = r.recognize_google(audio)
                        to_add = comlete_string(to_add)
                        print(f"to address is:\n{to_add}")
                        ta.speak("whats the mail")
                        audio = r.listen(source, timeout=10)
                        mail_body = r.recognize_google(audio)
                        print(f"mail is:\n{mail_body}")
                        tm.send_mail(email, to_add, password, mail_body)
                    zero_acc = [0] * 5
            # Stop symbol
            if sum(fingers) == 5:
                zero_acc[4] += 1
                if Accurate_ctr5 > Accuracy_factor:
                    exit()
                    zero_acc = [0] * 5
        # h, w, c = overlayList[0].shape
        # img[0:h, 0:w] = overlayList[0]
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow("image", img)
        # time.sleep(0.1)
        cv2.waitKey(1)
        if cv2.waitKey(1) == ord('q'):
            break


HandGesture()
