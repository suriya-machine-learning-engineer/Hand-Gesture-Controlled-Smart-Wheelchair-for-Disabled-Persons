def detect():
    import cv2
    import mediapipe as mp

    import serial
    serial_data = serial.Serial("Com7", 9600)

    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands

    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(
            model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
            max_num_hands=1) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue

            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            fingerCount = 0

            if results.multi_hand_landmarks:

                hand_landmarks = results.multi_hand_landmarks[0]
                handLabel = results.multi_handedness[0].classification[0].label

                handLandmarks = []

                for landmarks in hand_landmarks.landmark:
                    handLandmarks.append([landmarks.x, landmarks.y])

                if handLabel == "Left" and handLandmarks[4][0] > handLandmarks[3][0]:
                    fingerCount += 1
                elif handLabel == "Right" and handLandmarks[4][0] < handLandmarks[3][0]:
                    fingerCount += 1

                if handLandmarks[8][1] < handLandmarks[6][1]:  # Index finger
                    fingerCount += 1
                if handLandmarks[12][1] < handLandmarks[10][1]:  # Middle finger
                    fingerCount += 1
                if handLandmarks[16][1] < handLandmarks[14][1]:  # Ring finger
                    fingerCount += 1
                if handLandmarks[20][1] < handLandmarks[18][1]:  # Pinky
                    fingerCount += 1

                if fingerCount > 5:
                    fingerCount = 5

                # Determine command based on finger count
                command = ""
                if fingerCount == 1:
                    command = "Forward"
                    print(command)
                    serial_data.write(b'A')
                elif fingerCount == 2:
                    command = "Backward"
                    print(command)
                    serial_data.write(b'B')
                elif fingerCount == 3:
                    command = "Right"
                    print(command)
                    serial_data.write(b'C')
                elif fingerCount == 4:
                    command = "Left"
                    print(command)
                    serial_data.write(b'D')
                elif fingerCount == 5:
                    command = "Stop"
                    print(command)
                    serial_data.write(b'E')

                # Display command text on the window
                cv2.putText(image, command, (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 10)

                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

            cv2.imshow('Hands', image)
            if cv2.waitKey(5) & 0xFF == 27:
                break
    cap.release()



