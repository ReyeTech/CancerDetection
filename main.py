import cv2
from ultralytics import YOLO
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-v', '--video', required=True, help='Path to input video file')
ap.add_argument("-m", "--model", required=True, help="model to select")
args = ap.parse_args()

model = YOLO(args.model)

cap = cv2.VideoCapture(args.video)

while True:
    ret, frame = cap.read()

    if not ret:
        break 

    results = model.predict(source = frame, show = True, save = False)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
