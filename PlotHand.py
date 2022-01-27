import cv2
import mediapipe
from matplotlib import pyplot as plt


def CalcLandMarks():
    ret, img = cap.read()
    rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgbImg)  # results is a list of Hand objects
    # print(results.multi_hand_landmarks) # This will show the landmarks of all hands
    new_hand = []

    if results.multi_hand_landmarks:  # if results is not empty
        new_hand = []
        for hand in results.multi_hand_landmarks:  # For each hand in result
            for id, lm in enumerate(hand.landmark):  # For each landmark in hand
                hand_mk = [id, lm.x, lm.y, lm.z]
                new_hand.append(hand_mk)  # Append the landmark to new_hand

                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(cx, cy)
                # new_hand_mk = [id, cx, cy]
                # new_hand.append(new_hand_mk)

                if id == 8: cv2.circle(img, (cx, cy), 15, (0, 0, 255), -1)
                # if id == 4: cv2.circle(img, (cx, cy), 10, (0, 255, 255), -1)
                # if id == 12: cv2.circle(img, (cx, cy), 15, (255, 0, 0), -1)
                # if id == 16: cv2.circle(img, (cx, cy), 10, (0, 255, 0), -1)
                # if id == 20: cv2.circle(img, (cx, cy), 10, (255, 255, 0), -1)

            mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)  # Draw the landmarks

            print("Hand : ", new_hand)

    img = cv2.flip(img, 1)  # Flip the frame horizontally
    img = cv2.resize(img, (640, 480))  # increase frame size
    cv2.imshow('frame', img)  # Show the frame

    # Set up plot to call animate() function every 1000 milliseconds
    # ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)

    # plt.plot each hand_mk in new_hand concurrently
    return new_hand


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    mpHands = mediapipe.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mediapipe.solutions.drawing_utils  # For drawing landmarks

    while True:
        new_hand = CalcLandMarks()
        for hand_mk in new_hand:
            print("hand_mk",hand_mk)
            plt.plot(hand_mk[1], hand_mk[2], 'ro')

        plt.show(block=False)
        plt.pause(0.001)
        plt.clf()

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press q to quit
            break

    cap.release()
    cv2.destroyAllWindows()
