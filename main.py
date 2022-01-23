import cv2
import mediapipe
import numpy
import pyautogui


cap = cv2.VideoCapture(0)

mpHands = mediapipe.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
mpDraw = mediapipe.solutions.drawing_utils # For drawing landmarks

# pyautoGUI move mouse to the center of the screen
pyautogui.moveTo(pyautogui.size()[0]/2, pyautogui.size()[1]/2)

while True:
    ret, img = cap.read()
    rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgbImg) # results is a list of Hand objects
    #print(results.multi_hand_landmarks) # This will show the landmarks of all hands

    if results.multi_hand_landmarks: # if results is not empty
        for hand in results.multi_hand_landmarks: # For each hand in result
            for id, lm in enumerate(hand.landmark): # For each landmark in hand
                # print(id, lm) # Print the landmark id and its coordinates
                # Access each landmark in each Hand
                h , w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)   # Print the landmark id and its coordinates
                if id == 8:
                    cv2.circle(img, (cx, cy), 15, (0, 0, 255), -1)
                    # pyautoGUI move mouse with cx, cy with flipped horizontal axis (but in cx, cy size)
                    #pyautogui.moveTo(pyautogui.size()[0] - cx, cy)

                    # scale pyautoGUI move with cx, cy to screen size and flipped horizontal axis
                    pyautogui.moveTo(pyautogui.size()[0] - cx*pyautogui.size()[0]/w, cy*pyautogui.size()[1]/h)
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
