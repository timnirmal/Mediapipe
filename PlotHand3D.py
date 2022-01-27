import time
from mpl_toolkits import mplot3d
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

            # print("Hand : ", new_hand)

    img = cv2.flip(img, 1)  # Flip the frame horizontally
    img = cv2.resize(img, (640, 480))  # increase frame size
    cv2.imshow('frame', img)  # Show the frame

    # Set up plot to call animate() function every 1000 milliseconds
    # ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)

    # plt.plot each hand_marks in new_hand concurrently
    return all_hands


def PlotHand():
    all_hands = CalcLandMarks()  # Calculate landmarks for all hands
    hand_all_xs = []
    hand_all_ys = []
    hand_all_zs = []

    for new_hand in all_hands:
        hand_mk_xs = []
        hand_mk_ys = []
        hand_mk_zs = []
        for hand_mk in new_hand:
            hand_mk_xs.append(hand_mk[1])
            hand_mk_ys.append(hand_mk[2])
            hand_mk_zs.append(hand_mk[3])
        hand_all_xs.append(hand_mk_xs)
        hand_all_ys.append(hand_mk_ys)
        hand_all_zs.append(hand_mk_zs)

    ax = fig.add_subplot(111, projection='3d')
    ax.scatter3D(hand_all_xs, hand_all_ys, hand_all_zs, c='r', marker='o')

    plt.show(block=False)
    plt.pause(0.001)


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    mpHands = mediapipe.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mediapipe.solutions.drawing_utils  # For drawing landmarks

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


    # calculate time taken fo below process
    t = time.time()

    while True:
        print("New calculation\n\n")
        count = 0
        t = time.time()

        PlotHand()  # In here Hands are extracted from CalcLandMarks() and plotted.

        time_diff = time.time() - t
        count += 1
        time_avg = time_diff / count
        print("Time taken : ", time_diff)
        print("Average time taken : ", time_avg)

        plt.show(block=False)
        plt.pause(0.001)
        plt.clf()

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press q to quit
            break

    cap.release()
    cv2.destroyAllWindows()
