import mediapipe as mp
import cv2


class HandDetector:
    def __init__(self, mode=False, maxhands=2, detectionCon=0.5, trackcon=0.5):
        self.mode = mode
        self.maxHands = maxhands
        self.detectionCon = detectionCon
        self.trackCon = trackcon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectionCon,
                                        min_tracking_confidence=self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.dotsColor = self.mpDraw.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2)
        self.lineColor = self.mpDraw.DrawingSpec(color=(.124, 252, 0), thickness=3, circle_radius=2)

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        self.detectedPoints = self.hands.process(imgRGB)
        if self.detectedPoints.multi_hand_landmarks:
            for handCoOrdinates in self.detectedPoints.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handCoOrdinates, self.mpHands.HAND_CONNECTIONS, self.dotsColor,
                                               self.lineColor)
        return img

    def findPosition(self, img, handNo=0, draw=True):

        lmList = []
        if self.detectedPoints.multi_hand_landmarks:
            myHand = self.detectedPoints.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        return lmList


def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord("q"):
            break


if __name__ == "__main__":
    main()
