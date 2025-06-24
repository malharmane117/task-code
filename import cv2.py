import cv2
import face_recognition
import os

# Load known faces
known_faces = []
known_names = []

for filename in os.listdir("known_faces"):
    img = face_recognition.load_image_file(f"known_faces/{filename}")
    encoding = face_recognition.face_encodings(img)[0]
    known_faces.append(encoding)
    known_names.append(os.path.splitext(filename)[0])

# Start webcam
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    rgb_frame = frame[:, :, ::-1]  # BGR to RGB

    # Detect faces
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"

        if True in matches:
            index = matches.index(True)
            name = known_names[index]

        # Draw box
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        # Label
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    cv2.imshow("Face Detection & Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
