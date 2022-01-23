import cv2
import mediapipe
import numpy
import pyautogui


cap = cv2.VideoCapture(0)

mpHands = mediapipe.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
mpDraw = mediapipe.solutions.drawing_utils # For drawing landmarks

while True:
    ret, img = cap.read()
    rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgbImg) # results is a list of Hand objects
    print(results.multi_hand_landmarks) # This will show the landmarks of all hands

    if results.multi_hand_landmarks: # if results is not empty
        for hand in results.multi_hand_landmarks: # For each hand in result
            mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS) # Draw the landmarks



    if not ret:
        break
    # flip the frame horizontally
    img = cv2.flip(img, 1)
    # increase frame size
    img = cv2.resize(img, (640, 480))
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()














print(pyautogui.position())

#x = 100
#y = 100

#for i in range (10):
#    x = x + 100
#    y = y + 50
#    pyautogui.moveTo(x,y)
    # use pyautogui.move(x,y) to move the mouse x,y relative to the current position


# finger tracking with mediapipe
