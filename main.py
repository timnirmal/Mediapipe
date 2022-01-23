import cv2
import mediapipe
import numpy
import pyautogui

cap = cv2.VideoCapture(0)

mpHands = mediapipe.solutions.hands
hands = mpHands.Hands()
mpDraw = mediapipe.solutions.drawing_utils  # For drawing landmarks

# pyautoGUI move mouse to the center of the screen
# pyautogui.moveTo(pyautogui.size()[0]/2, pyautogui.size()[1]/2)


id8_positions = []
id4_positions = []
id12_positions = []
position_list = []

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

                if id == 8:
                    cv2.circle(img, (cx, cy), 15, (0, 0, 255), -1)
                    # pyautoGUI move mouse with cx, cy with flipped horizontal axis (but in cx, cy size)
                    # pyautogui.moveTo(pyautogui.size()[0] - cx, cy)
                    # draw rectangle around the landmark
                    size = 80
                    cv2.rectangle(img, (cx - size, cy - size), (cx + size, cy + size), (0, 255, 0), 2)

                    # scale pyautoGUI move with cx, cy to screen size and flipped horizontal axis
                    pyautogui.moveTo(pyautogui.size()[0] - cx * pyautogui.size()[0] / w, cy * pyautogui.size()[1] / h)
                    # clear id8_positions
                    # id8_positions.clear()
                    # append cx and cy to id8_positions
                    # id8_positions = [(cx, cy)]
                    # print("8 -> ", end=" ")
                    # print(id8_positions)

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

                    # if gap between lastPosition_x and cx is less than 40, and gap between lastPosition_y and cy is
                    # less than 40, then move mouse to the center of the screen
                    if abs(lastPosition_8x - cx) < 40 and abs(lastPosition_8y - cy) < 40:  # Click Method
                        # if gap between lastPosition_8x and cx is less than 40, and gap between
                        # lastPosition_8y and cy is less than 40, then move mouse to the center of the screen
                        if abs(lastPosition_8x - lastPosition_4x) > 80:
                            pyautogui.click(button='right',interval=0.1)
                        else:
                            pyautogui.click(interval=0.1)
                        # clear id12_positions
                        # id12_positions.clear()
                        # append cx and cy to id12_positions
                        # id12_positions = [(cx, cy)]
                        # print("12 -> ", end=" ")
                        # print(id12_positions)

                # Double Click
                """
                if id == 4:
                    cv2.circle(img, (cx, cy), 15, (0, 255, 255), -1)

                    # print("8 -> ", end=" ")
                    # print(id8_positions)
                    # print("12 -> ", end=" ")
                    # print(id12_positions)

                    # if id8_positions is not empty
                    if id8_positions and id12_positions:
                        # lastPosition_x and lastPosition_y of id12_positions
                        lastPosition_12x = id8_positions[-1][0]
                        lastPosition_12y = id8_positions[-1][1]

                        # lastPosition_4x and lastPosition_4y of id4_positions
                        lastPosition_8x = id8_positions[-1][0]
                        lastPosition_8y = id8_positions[-1][1]

                        # if gap between lastPosition_8x and cx is less than 40, and gap between
                        # lastPosition_8y and cy is less than 40, then move mouse to the center of the screen
                        if abs(lastPosition_8x - cx) > 80:
                            print("Done")
                            # if gap between lastPosition_4x and lastPosition_12x is less than 40, and gap between
                            # lastPosition_4y and lastPosition_12y is less than 40, then move mouse to the center of the
                            # screen
                            if abs(lastPosition_12x - lastPosition_8x) < 40 and abs(lastPosition_12y - lastPosition_8y) < 40:
                                print("Double Click")
                                pyautogui.doubleClick(interval=0.5)

                """
                """
                # if lm.z is negative, move mouse up
                if lm.z < 0:
                    pyautogui.moveRel(0, -lm_z_avg*pyautogui.size()[1]/h)
                # if lm.z is positive, move mouse down
                elif lm.z > 0:
                    pyautogui.moveRel(0, lm_z_avg*pyautogui.size()[1]/h)
                # if lm.z is 0, move mouse to center
                else:
                    pyautogui.moveTo(pyautogui.size()[0]/2, pyautogui.size()[1]/2)
                """

            mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)  # Draw the landmarks

    if not ret:
        break
    img = cv2.flip(img, 1)  # Flip the frame horizontally
    img = cv2.resize(img, (640, 480))  # increase frame size
    cv2.imshow('frame', img)  # Show the frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press q to quit
        break

cap.release()
cv2.destroyAllWindows()

print(pyautogui.position())

# x = 100
# y = 100

# for i in range (10):
#    x = x + 100
#    y = y + 50
#    pyautogui.moveTo(x,y)
# use pyautogui.move(x,y) to move the mouse x,y relative to the current position


# finger tracking with mediapipe
