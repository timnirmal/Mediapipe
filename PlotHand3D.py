import time
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
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

    # Hand line start
    hand_all_xs_start = []
    hand_all_ys_start = []
    hand_all_zs_start = []

    # Hand line end
    hand_all_xs_end = []
    hand_all_ys_end = []
    hand_all_zs_end = []

    for new_hand in all_hands:  # for each hand in hand set
        print("Hand : ", new_hand)
        hand_mk_xs = []
        hand_mk_ys = []
        hand_mk_zs = []
        for hand_mk in new_hand:  # for each hand mark in a hand
            hand_mk_xs.append(hand_mk[1])
            hand_mk_ys.append(hand_mk[2])
            hand_mk_zs.append(hand_mk[3])

            # draw line between 3 and 4, 3 and 2, 2 and 1, 1 and 0 with color (0, 255, 255)
            # 0 and 1
            if hand_mk[0] == 0:
                hand_all_xs_start.append(hand_mk[1])
                hand_all_ys_start.append(hand_mk[2])
                hand_all_zs_start.append(hand_mk[3])
                hand_all_xs_end.append(new_hand[1][1])
                hand_all_ys_end.append(new_hand[1][2])
                hand_all_zs_end.append(new_hand[1][3])
            # 0 and 5
                hand_all_xs_start.append(hand_mk[1])
                hand_all_ys_start.append(hand_mk[2])
                hand_all_zs_start.append(hand_mk[3])
                hand_all_xs_end.append(new_hand[5][1])
                hand_all_ys_end.append(new_hand[5][2])
                hand_all_zs_end.append(new_hand[5][3])
            # 0 and 17
                hand_all_xs_start.append(hand_mk[1])
                hand_all_ys_start.append(hand_mk[2])
                hand_all_zs_start.append(hand_mk[3])
                hand_all_xs_end.append(new_hand[17][1])
                hand_all_ys_end.append(new_hand[17][2])
                hand_all_zs_end.append(new_hand[17][3])

            # 1 and 2
            if hand_mk[0] == 1:
                hand_all_xs_start.append(hand_mk[1])
                hand_all_ys_start.append(hand_mk[2])
                hand_all_zs_start.append(hand_mk[3])
                hand_all_xs_end.append(new_hand[2][1])
                hand_all_ys_end.append(new_hand[2][2])
                hand_all_zs_end.append(new_hand[2][3])
            # 2 and 3
            if hand_mk[0] == 2:
                hand_all_xs_start.append(hand_mk[1])
                hand_all_ys_start.append(hand_mk[2])
                hand_all_zs_start.append(hand_mk[3])
                hand_all_xs_end.append(new_hand[3][1])
                hand_all_ys_end.append(new_hand[3][2])
                hand_all_zs_end.append(new_hand[3][3])
            # 3 and 4
            if hand_mk[0] == 3:
                hand_all_xs_start.append(hand_mk[1])
                hand_all_ys_start.append(hand_mk[2])
                hand_all_zs_start.append(hand_mk[3])
                hand_all_xs_end.append(new_hand[4][1])
                hand_all_ys_end.append(new_hand[4][2])
                hand_all_zs_end.append(new_hand[4][3])

            # 5 and 6
            if hand_mk[0] == 5:
                hand_all_xs_start.append(hand_mk[1])
                hand_all_ys_start.append(hand_mk[2])
                hand_all_zs_start.append(hand_mk[3])
                hand_all_xs_end.append(new_hand[6][1])
                hand_all_ys_end.append(new_hand[6][2])
                hand_all_zs_end.append(new_hand[6][3])
            # 6 and 7
            if hand_mk[0] == 6:
                hand_all_xs_start.append(hand_mk[1])
                hand_all_ys_start.append(hand_mk[2])
                hand_all_zs_start.append(hand_mk[3])
                hand_all_xs_end.append(new_hand[7][1])
                hand_all_ys_end.append(new_hand[7][2])
                hand_all_zs_end.append(new_hand[7][3])
            # 7 and 8
            if hand_mk[0] == 7:
                hand_all_xs_start.append(hand_mk[1])
                hand_all_ys_start.append(hand_mk[2])
                hand_all_zs_start.append(hand_mk[3])
                hand_all_xs_end.append(new_hand[8][1])
                hand_all_ys_end.append(new_hand[8][2])
                hand_all_zs_end.append(new_hand[8][3])

            # 9 and 10
            if hand_mk[0] == 9:
                hand_all_xs_start.append(hand_mk[1])
                hand_all_ys_start.append(hand_mk[2])
                hand_all_zs_start.append(hand_mk[3])
                hand_all_xs_end.append(new_hand[10][1])
                hand_all_ys_end.append(new_hand[10][2])
                hand_all_zs_end.append(new_hand[10][3])
            # 10 and 11
            if hand_mk[0] == 10:
                hand_all_xs_start.append(hand_mk[1])
                hand_all_ys_start.append(hand_mk[2])
                hand_all_zs_start.append(hand_mk[3])
                hand_all_xs_end.append(new_hand[11][1])
                hand_all_ys_end.append(new_hand[11][2])
                hand_all_zs_end.append(new_hand[11][3])
            # 11 and 12
            if hand_mk[0] == 11:
                hand_all_xs_start.append(hand_mk[1])
                hand_all_ys_start.append(hand_mk[2])
                hand_all_zs_start.append(hand_mk[3])
                hand_all_xs_end.append(new_hand[12][1])
                hand_all_ys_end.append(new_hand[12][2])
                hand_all_zs_end.append(new_hand[12][3])

            # 13 and 14
            if hand_mk[0] == 13:
                hand_all_xs_start.append(hand_mk[1])
                hand_all_ys_start.append(hand_mk[2])
                hand_all_zs_start.append(hand_mk[3])
                hand_all_xs_end.append(new_hand[14][1])
                hand_all_ys_end.append(new_hand[14][2])
                hand_all_zs_end.append(new_hand[14][3])
            # 14 and 15
            if hand_mk[0] == 14:
                hand_all_xs_start.append(hand_mk[1])
                hand_all_ys_start.append(hand_mk[2])
                hand_all_zs_start.append(hand_mk[3])
                hand_all_xs_end.append(new_hand[15][1])
                hand_all_ys_end.append(new_hand[15][2])
                hand_all_zs_end.append(new_hand[15][3])
            # 15 and 16
            if hand_mk[0] == 15:
                hand_all_xs_start.append(hand_mk[1])
                hand_all_ys_start.append(hand_mk[2])
                hand_all_zs_start.append(hand_mk[3])
                hand_all_xs_end.append(new_hand[16][1])
                hand_all_ys_end.append(new_hand[16][2])
                hand_all_zs_end.append(new_hand[16][3])

            # 17 and 18
            if hand_mk[0] == 17:
                hand_all_xs_start.append(hand_mk[1])
                hand_all_ys_start.append(hand_mk[2])
                hand_all_zs_start.append(hand_mk[3])
                hand_all_xs_end.append(new_hand[18][1])
                hand_all_ys_end.append(new_hand[18][2])
                hand_all_zs_end.append(new_hand[18][3])
            # 18 and 19
            if hand_mk[0] == 18:
                hand_all_xs_start.append(hand_mk[1])
                hand_all_ys_start.append(hand_mk[2])
                hand_all_zs_start.append(hand_mk[3])
                hand_all_xs_end.append(new_hand[19][1])
                hand_all_ys_end.append(new_hand[19][2])
                hand_all_zs_end.append(new_hand[19][3])
            # 19 and 20
            if hand_mk[0] == 19:
                hand_all_xs_start.append(hand_mk[1])
                hand_all_ys_start.append(hand_mk[2])
                hand_all_zs_start.append(hand_mk[3])
                hand_all_xs_end.append(new_hand[20][1])
                hand_all_ys_end.append(new_hand[20][2])
                hand_all_zs_end.append(new_hand[20][3])


        hand_all_xs.append(hand_mk_xs)
        hand_all_ys.append(hand_mk_ys)
        hand_all_zs.append(hand_mk_zs)

    ax = fig.add_subplot(111, projection='3d')
    # limit graph in -1 and 1
    ax.set_xlim3d(0, 1)
    ax.set_ylim3d(0, 1)
    #ax.set_zlim3d(-0.3, 0.8)

    # show x , y , z on graph
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')



    ax.scatter3D(hand_all_xs, hand_all_ys, hand_all_zs, c='r', marker='o')
    # change color of hand_all_xs[0], hand_all_ys[0], hand_all_zs[0] point
    if hand_all_xs and hand_all_ys and hand_all_zs:
        ax.scatter3D(hand_all_xs[0][0], hand_all_ys[0][0], hand_all_zs[0][0], c='k', marker='o')
        ax.scatter3D(hand_all_xs[0][4], hand_all_ys[0][4], hand_all_zs[0][4], c='c', marker='x')
        ax.scatter3D(hand_all_xs[0][8], hand_all_ys[0][8], hand_all_zs[0][8], c='g', marker='x')
        ax.scatter3D(hand_all_xs[0][12], hand_all_ys[0][12], hand_all_zs[0][12], c='g', marker='x')
        ax.scatter3D(hand_all_xs[0][16], hand_all_ys[0][16], hand_all_zs[0][16], c='g', marker='x')
        ax.scatter3D(hand_all_xs[0][20], hand_all_ys[0][20], hand_all_zs[0][20], c='m', marker='x')

    # ax.scatter3D(hand_all_xs_start, hand_all_ys_start, hand_all_zs_start, c='b', marker='o')
    ax.plot(hand_all_xs_start, hand_all_ys_start, hand_all_zs_start, 'b')

    # flip x and y axis
    #ax.invert_xaxis()
    #ax.invert_zaxis()

    # rotate graph
    ax.view_init(elev=90, azim=90)




    plt.show(block=False)
    Axes3D.plot(ax, hand_all_xs_end, hand_all_ys_end, hand_all_zs_end, 'b')
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
