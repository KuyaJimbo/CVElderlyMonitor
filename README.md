# ElderGuard: Real-Time Fall Detection System

ElderGuard is a real-time pose detection system designed to enhance the safety of elderly individuals in care facilities. The system monitors live video feeds and alerts caregivers when a person is detected lying down for too long, reducing the risk of injuries caused by unnoticed falls. With a simple interface, instant sound alerts, and event logging, ElderGuard ensures caregivers can respond quickly and efficiently.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Overview
Falls are a leading cause of injury among the elderly, especially in nursing homes and care facilities. ElderGuard addresses this issue by using real-time video monitoring and pose detection to alert caregivers when a person has been lying down for too long. The system helps prevent falls from going unnoticed, ensuring faster intervention and improving safety.

## Features
- **Real-Time Pose Detection**: Detects when a person is lying down using computer vision and pose estimation.
- **Sound Alerts**: Plays an audio alert when a person is detected lying down for an extended period.
- **Event Logging**: Automatically logs detection events with timestamps for caregiver review.
- **Simple Interface**: Provides a user-friendly interface for caregivers to monitor the elderly and respond quickly.
- **Settings**: Adjustable alert threshold to fine-tune the sensitivity based on user preferences.

## Tech Stack
- **Flask**: Web framework for serving the application.
- **OpenCV**: Used for video stream processing and frame analysis.
- **MediaPipe**: For real-time pose detection.
- **Socket.IO**: Enables real-time communication between the frontend and backend.
- **HTML/CSS/JavaScript**: For building the user interface and handling frontend interactions.
- **Python**: Backend language for managing pose detection and server logic.

## Installation
To set up and run ElderGuard locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/KuyaJimbo/elderguard.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd elderguard
    ```
3. **Create a virtual environment (optional but recommended)**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. **Run the application**:
    ```bash
    python app.py
    ```
5. **Access the application**:
    Open your web browser and navigate to `http://localhost:5000`.

## Usage
Once the application is running, you will see a live video feed in your browser. The system will automatically detect if a person is lying down for more than the configured threshold (e.g., 2 seconds). When this happens:
- An **audio alert** will play.
- The person’s status will turn red in the interface.
- The event will be **logged** with a timestamp in the event log panel.

You can reset the person’s status using the **Reset** button, and the system will log the reset event.

## Contributing
If you'd like to contribute to ElderGuard, feel free to fork the repository and submit a pull request with your improvements. We welcome contributions, especially in the following areas:
- Future Stuff 
