import cv2
import openpyxl
from openpyxl import Workbook
from datetime import datetime


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
wb = Workbook()
ws = wb.active
ws.append(["Name", "Time"])

def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # FOR WEB SQUARE FACECAM
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        ws.append(["Unknown", current_time])

    return image

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame by frame
    ret, frame = video_capture.read()

    # Detect faces in the frame and log attendance
    frame_with_faces = detect_faces(frame)

    # Display the resulting frame
    cv2.imshow('Face Detection', frame_with_faces)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

file_path = "D:/attendance.xlsx"


wb.save(file_path)


video_capture.release()
cv2.destroyAllWindows()
