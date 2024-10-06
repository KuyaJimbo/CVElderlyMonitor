# CVElderlyMonitor

This project is a Python application that uses OpenCV and MediaPipe to detect human poses in a video stream and overlay a skeleton on the detected poses in real-time.

## Features

- Real-time human pose detection
- Skeleton overlay on detected poses
- Works with live video feed from a camera or video file input

## Requirements

- Python 3.7+
- OpenCV
- MediaPipe
- NumPy

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/kuyajimbo/CVElderlyMonitor.git
   cd Elderlymonitor
   ```

2. Install the required packages:
   ```
   pip install opencv-python mediapipe numpy
   ```

## Usage

1. Run the script:
   ```
   python app.py
   ```

2. The application will open your default camera feed and start detecting poses.

3. Press 'q' to quit the application.


## Customization

- To use a video file instead of a camera feed, change the `cv2.VideoCapture(0)` line to `cv2.VideoCapture('path/to/your/video.mp4')`.
- Adjust the `min_detection_confidence` and `min_tracking_confidence` parameters in the `mp_pose.Pose()` function to fine-tune the pose detection.

## Contributing

Contributions to improve the application are welcome. Please feel free to submit a Pull Request.

## Acknowledgments

- OpenCV team for the computer vision library
- Google's MediaPipe team for the pose estimation model
