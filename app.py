import cv2
import mediapipe as mp
import numpy as np
import base64
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Function to check if the person is lying down
def is_person_lying_down(landmarks):
    # Get y-coordinates for shoulders, hips, and head
    left_shoulder_y = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER].y
    right_shoulder_y = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER].y
    left_hip_y = landmarks[mp_pose.PoseLandmark.LEFT_HIP].y
    right_hip_y = landmarks[mp_pose.PoseLandmark.RIGHT_HIP].y
    nose_y = landmarks[mp_pose.PoseLandmark.NOSE].y

    # Calculate the average y-coordinate for shoulders and hips
    avg_shoulder_y = (left_shoulder_y + right_shoulder_y) / 2
    avg_hip_y = (left_hip_y + right_hip_y) / 2

    # Check if shoulders, hips, and nose are nearly aligned horizontally (small vertical difference)
    if abs(avg_shoulder_y - avg_hip_y) < 0.05 and abs(avg_shoulder_y - nose_y) < 0.05:
        print("shoulders, hips, and nose are nearly aligned horizontally")
        return True

    return False

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('frame')
def handle_frame(data):
    # Decode the base64 image
    img_data = base64.b64decode(data.split(',')[1])
    nparr = np.frombuffer(img_data, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert the image from BGR to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image and detect pose
    result = pose.process(frame_rgb)

    is_lying_down = False
    if result.pose_landmarks:
        # Check if the person is lying down (without drawing the skeleton)
        is_lying_down = is_person_lying_down(result.pose_landmarks.landmark)

    # Convert the frame back to BGR for encoding
    frame_bgr = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)

    # Encode the frame as a JPEG image
    _, buffer = cv2.imencode('.jpg', frame_bgr)
    frame_base64 = base64.b64encode(buffer).decode('utf-8')

    # Send the result (without skeleton) back to the client
    socketio.emit('pose_result', {'is_lying_down': is_lying_down, 'image': f'data:image/jpeg;base64,{frame_base64}'})

if __name__ == '__main__':
    socketio.run(app, debug=True)
