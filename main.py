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
    #print(results.multi_hand_landmarks) # This will show the landmarks of all hands

    if results.multi_hand_landmarks: # if results is not empty
        for hand in results.multi_hand_landmarks: # For each hand in result
            for id, lm in enumerate(hand.landmark): # For each landmark in hand
                # print(id, lm) # Print the landmark id and its coordinates
                h , w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)   # Print the landmark id and its coordinates
                if id == 8:
                    cv2.circle(img, (cx, cy), 15, (0, 0, 255), -1)
            mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS) # Draw the landmarks



    if not ret:
        break
    img = cv2.flip(img, 1)    # Flip the frame horizontally
    img = cv2.resize(img, (640, 480))   # increase frame size
    cv2.imshow('frame', img)    # Show the frame

    if cv2.waitKey(1) & 0xFF == ord('q'): # Press q to quit
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
