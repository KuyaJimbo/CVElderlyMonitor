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
   git clone https://github.com/yourusername/opencv-skeleton-overlay.git
   cd opencv-skeleton-overlay
   ```

2. Install the required packages:
   ```
   pip install opencv-python mediapipe numpy
   ```

## Usage

1. Run the script:
   ```
   python skeleton_overlay.py
   ```

2. The application will open your default camera feed and start detecting poses.

3. Press 'q' to quit the application.

## Google Colab Usage

To run this application in Google Colab:

1. Upload the `skeleton_overlay.py` file to your Colab notebook.

2. Install the required libraries:
   ```
   !pip install mediapipe opencv-python-headless
   ```

3. Modify the script to use `cv2_imshow` instead of `cv2.imshow`:
   ```python
   from google.colab.patches import cv2_imshow
   # Replace cv2.imshow('Skeleton Overlay', frame) with:
   cv2_imshow(frame)
   ```

4. Remove the `cv2.waitKey(1)` line as it's not needed in Colab.

5. To capture video in Colab, add this at the beginning of your code:
   ```python
   from google.colab import output
   output.enable_custom_widget_manager()
   ```

## Customization

- To use a video file instead of a camera feed, change the `cv2.VideoCapture(0)` line to `cv2.VideoCapture('path/to/your/video.mp4')`.
- Adjust the `min_detection_confidence` and `min_tracking_confidence` parameters in the `mp_pose.Pose()` function to fine-tune the pose detection.

## Contributing

Contributions to improve the application are welcome. Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- OpenCV team for the computer vision library
- Google's MediaPipe team for the pose estimation model
