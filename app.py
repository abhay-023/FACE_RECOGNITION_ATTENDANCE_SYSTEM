from flask import Flask, render_template, Response, request
import cv2
import face_recognition
import os
import numpy as np
import pandas as pd
from datetime import datetime

app = Flask(__name__)

camera = cv2.VideoCapture(0)
KNOWN_FACES_DIR = "known_faces"

if not os.path.exists(KNOWN_FACES_DIR):
    os.makedirs(KNOWN_FACES_DIR)

# Load known faces
known_encodings = []
known_names = []

def load_faces():
    known_encodings.clear()
    known_names.clear()
    for filename in os.listdir(KNOWN_FACES_DIR):
        image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{filename}")
        encoding = face_recognition.face_encodings(image)[0]
        known_encodings.append(encoding)
        known_names.append(filename.split(".")[0])


load_faces()

def mark_attendance(name):
    df = pd.read_csv("attendance.csv")
    if name not in df['Name'].values:
        now = datetime.now()
        df.loc[len(df)] = [name, now.strftime("%H:%M:%S"), now.strftime("%d-%m-%Y")]
        df.to_csv("attendance.csv", index=False)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, faces)

        for encoding, location in zip(encodings, faces):
            matches = face_recognition.compare_faces(known_encodings, encoding)
            name = "Unknown"

            if True in matches:
                index = matches.index(True)
                name = known_names[index]
                mark_attendance(name)

            top, right, bottom, left = location
            cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
            cv2.putText(frame, name, (left, top-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        success, frame = camera.read()
        cv2.imwrite(f"{KNOWN_FACES_DIR}/{name}.jpg", frame)
        load_faces()
    return render_template('register.html')

@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    if not os.path.exists("attendance.csv"):
        pd.DataFrame(columns=["Name", "Time", "Date"]).to_csv("attendance.csv",
                                                               index=False)
    app.run(debug=True)



# def load_faces():
#     for filename in os.listdir("known_faces"):
#         if filename.endswith((".jpg", ".png", ".jpeg")):
#             path = os.path.join("known_faces", filename)
#             image = face_recognition.load_image_file(path)
#             encodings = face_recognition.face_encodings(image)
#             if len(encodings) > 0:
#                 encoding = encodings[0]
#                 known_face_encodings.append(encoding)
#                 known_face_names.append(os.path.splitext(filename)[0])
#                 print(f"[LOADED] Face found in {filename}")
#             else:
#                 print(f"[WARNING] No face found in {filename}, skipping...")


