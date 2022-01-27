import cv2
import mediapipe
import numpy as np

cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(3, 1280)
cap.set(4, 720)

# 640, 480

mpHands = mediapipe.solutions.hands
hands = mpHands.Hands()
mpDraw = mediapipe.solutions.drawing_utils  # For drawing landmarks

id8_positions = []
id4_positions = []
id12_positions = []
position_list = []
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)

brushSize = 10

# print cap resolution
print(cap.get(3), cap.get(4))
# print imgCanvas resolution
print(imgCanvas.shape)

while True:
    ret, img = cap.read()
    rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgbImg)  # results is a list of Hand objects
    # print(results.multi_hand_landmarks) # This will show the landmarks of all hands

    if results.multi_hand_landmarks:  # if results is not empty
        for hand in results.multi_hand_landmarks:  # For each hand in result
            for id, lm in enumerate(hand.landmark):  # For each landmark in hand
                # print(id, lm) # Print the landmark id and its coordinates
                # Access each landmark in each Hand
                # print(lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)   # Print the landmark id and its coordinates

                # for each id, cx, cy, append to the list
                if id == 8:
                    # if id8_positions have 20 elements, delete the first element
                    if len(id8_positions) == 20:
                        id8_positions.pop(0)
                    id8_positions.append((cx, cy))
                elif id == 4:
                    if len(id4_positions) == 20:
                        id4_positions.pop(0)
                    id4_positions.append((cx, cy))
                elif id == 12:
                    if len(id12_positions) == 20:
                        id12_positions.pop(0)
                    id12_positions.append((cx, cy))

                # Single CLick
                if id == 12:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 0), -1)

                    # lastPosition_x and lastPosition_y of id8_positions
                    lastPosition_8x = id8_positions[-1][0]
                    lastPosition_8y = id8_positions[-1][1]

                    # lastPosition_x and lastPosition_y of id4_positions
                    lastPosition_4x = id4_positions[-1][0]
                    lastPosition_4y = id4_positions[-1][1]
                    # TODO: Remove Lists and Set only variables at the beginning

                    # lastPosition_x and lastPosition_y of id12_positions
                    lastPosition_12x = id12_positions[-1][0]

                    # if gap between lastPosition_x and cx is less than 40, and gap between lastPosition_y and cy is
                    # less than 40, then move mouse to the center of the screen
                    if abs(lastPosition_8x - cx) < 40 and abs(lastPosition_8y - cy) < 40:  # Click Method
                        # if gap between lastPosition_8x and cx is less than 40, and gap between
                        # lastPosition_8y and cy is less than 40, then move mouse to the center of the screen
                        if abs(lastPosition_8x - lastPosition_4x) > 80:
                            cv2.circle(img, (cx, cy), 15, (0, 0, 255), -1)
                        else:
                            if xp == 0 and yp == 0:
                                xp, yp = cx, cy
                            cv2.line(img, (xp, yp), (cx, cy), (0, 255, 0), brushSize)
                            cv2.line(imgCanvas, (xp, yp), (cx, cy), (0, 255, 0), brushSize)
                    xp, yp = cx, cy

            mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)  # Draw the landmarks

    if not ret:
        break

    imgInv = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgInv, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    img = cv2.flip(img, 1)  # Flip the frame horizontally
    cv2.imshow('frame', img)  # Show the frame
    #imgCanvas2 = cv2.flip(imgCanvas, 1)  # Flip the frame horizontally
    #cv2.imshow('frameCanvas', imgCanvas2)  # Show the frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press q to quit
        break

cap.release()
cv2.destroyAllWindows()
