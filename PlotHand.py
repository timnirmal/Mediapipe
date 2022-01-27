import time

import cv2
import mediapipe
from matplotlib import pyplot as plt


def CalcLandMarks():
    ret, img = cap.read()
    rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgbImg)  # results is a list of Hand objects
    # print(results.multi_hand_landmarks) # This will show the landmarks of all hands

    all_hands = []
    if results.multi_hand_landmarks:  # if results is not empty
        new_hand = []
        for hand in results.multi_hand_landmarks:  # For each hand in result
            new_hand = []
            for id, lm in enumerate(hand.landmark):  # For each landmark in hand
                hand_marks = [id, lm.x, lm.y, lm.z]
                new_hand.append(hand_marks)  # Append the landmark to new_hand

                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(cx, cy)
                # new_hand_mk = [id, cx, cy]
                # new_hand.append(new_hand_mk)

                if id == 4: cv2.circle(img, (cx, cy), 10, (0, 255, 255), -1)
                if id == 8: cv2.circle(img, (cx, cy), 15, (0, 0, 255), -1)
                if id == 12: cv2.circle(img, (cx, cy), 15, (255, 0, 0), -1)
                if id == 16: cv2.circle(img, (cx, cy), 10, (0, 255, 0), -1)
                if id == 20: cv2.circle(img, (cx, cy), 10, (255, 255, 0), -1)

            mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)  # Draw the landmarks
            all_hands.append(new_hand)  # Append the new_hand to all_hands

            print("Hand : ", new_hand)

    img = cv2.flip(img, 1)  # Flip the frame horizontally
    img = cv2.resize(img, (640, 480))  # increase frame size
    cv2.imshow('frame', img)  # Show the frame

    # Set up plot to call animate() function every 1000 milliseconds
    # ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)

    # plt.plot each hand_marks in new_hand concurrently
    return all_hands


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    mpHands = mediapipe.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mediapipe.solutions.drawing_utils  # For drawing landmarks

    while True:
        all_hands = CalcLandMarks()
        print("New calculation\n\n")
        i = 0
        # calculate time taken fo below process
        t = time.time()

        for new_hand in all_hands:
            for hand_mk in new_hand:
                print("hand_mk",new_hand[4])
                plt.plot(hand_mk[1], hand_mk[2], 'ro')
                # draw line between 3 and 4, 3 and 2, 2 and 1, 1 and 0 with color (0, 255, 255)
                plt.plot([new_hand[3][1], new_hand[4][1]], [new_hand[3][2], new_hand[4][2]], 'c')
                plt.plot([new_hand[2][1], new_hand[3][1]], [new_hand[2][2], new_hand[3][2]], 'c')
                plt.plot([new_hand[1][1], new_hand[2][1]], [new_hand[1][2], new_hand[2][2]], 'c')
                plt.plot([new_hand[0][1], new_hand[1][1]], [new_hand[0][2], new_hand[1][2]], 'c')

                # draw line between 8 and 7, 7 and 6, 6 and 5, 5 and 0 with color red
                plt.plot([new_hand[7][1], new_hand[8][1]], [new_hand[7][2], new_hand[8][2]], 'r')
                plt.plot([new_hand[6][1], new_hand[7][1]], [new_hand[6][2], new_hand[7][2]], 'r')
                plt.plot([new_hand[5][1], new_hand[6][1]], [new_hand[5][2], new_hand[6][2]], 'r')
                plt.plot([new_hand[0][1], new_hand[5][1]], [new_hand[0][2], new_hand[5][2]], 'r')

    
                # draw line between 12 and 11, 11 and 10, 10 and 9 with color blue
                plt.plot([new_hand[11][1], new_hand[12][1]], [new_hand[11][2], new_hand[12][2]], 'b')
                plt.plot([new_hand[10][1], new_hand[11][1]], [new_hand[10][2], new_hand[11][2]], 'b')
                plt.plot([new_hand[9][1], new_hand[10][1]], [new_hand[9][2], new_hand[10][2]], 'b')
                plt.plot([new_hand[0][1], new_hand[9][1]], [new_hand[0][2], new_hand[9][2]], 'b')
    
                # draw line between 16 and 15, 15 and 14, 14 and 13 with color green
                plt.plot([new_hand[15][1], new_hand[16][1]], [new_hand[15][2], new_hand[16][2]], 'g')
                plt.plot([new_hand[14][1], new_hand[15][1]], [new_hand[14][2], new_hand[15][2]], 'g')
                plt.plot([new_hand[13][1], new_hand[14][1]], [new_hand[13][2], new_hand[14][2]], 'g')
                plt.plot([new_hand[0][1], new_hand[13][1]], [new_hand[0][2], new_hand[13][2]], 'g')
    
                # draw line between 20 and 19, 19 and 18, 18 and 17, 17 and 0 with color yellow
                plt.plot([new_hand[19][1], new_hand[20][1]], [new_hand[19][2], new_hand[20][2]], 'y')
                plt.plot([new_hand[18][1], new_hand[19][1]], [new_hand[18][2], new_hand[19][2]], 'y')
                plt.plot([new_hand[17][1], new_hand[18][1]], [new_hand[17][2], new_hand[18][2]], 'y')
                plt.plot([new_hand[0][1], new_hand[17][1]], [new_hand[0][2], new_hand[17][2]], 'y')


                print("Done")
                i += 1

        print("Time taken : ", time.time() - t)

        plt.show(block=False)
        plt.pause(0.001)
        plt.clf()

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press q to quit
            break

    cap.release()
    cv2.destroyAllWindows()
