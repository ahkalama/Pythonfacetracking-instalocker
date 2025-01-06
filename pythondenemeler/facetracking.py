import cv2
import pyautogui
import gc

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

try:
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Kamera açılamadı!")
        exit()

    while True:

        ret, frame = cap.read()
        if not ret:
            print("Kameradan görüntü alınamadı!")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            face_center_x = x + w // 2
            face_center_y = y + h // 2


            pyautogui.moveTo(face_center_x, face_center_y)


        cv2.imshow('Kamera Yüz Takibi', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:

    if 'cap' in locals() and cap.isOpened():
        cap.release()
    cv2.destroyAllWindows()
    gc.collect()
