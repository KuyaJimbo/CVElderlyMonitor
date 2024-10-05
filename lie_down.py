import cv2
import mediapipe as mp

# Initialize MediaPipe Pose class
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Initialize MediaPipe Drawing class
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Start capturing video from webcam
cap = cv2.VideoCapture(0)

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
        return True
    return False
id = 0
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Convert the image from BGR to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image and detect pose
    result = pose.process(frame_rgb)

    # If pose landmarks are found, draw them and check if the person is lying down
    if result.pose_landmarks:
        # Draw landmarks and connections on the frame
        mp_drawing.draw_landmarks(
            frame, 
            result.pose_landmarks, 
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
        )

        # Check if the person is lying down
        if is_person_lying_down(result.pose_landmarks.landmark):
            id += 1
            print("Person is lying down!", id)

    # Show the frame with the skeleton drawn
    cv2.imshow('Skeleton Detection', frame)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
