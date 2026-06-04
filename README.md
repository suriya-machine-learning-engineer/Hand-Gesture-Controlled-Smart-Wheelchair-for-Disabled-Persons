
# Hand Gesture Controlled Smart Wheelchair for Disabled Persons

## Overview

Hand Gesture Controlled Smart Wheelchair is an assistive technology project designed to help physically challenged and disabled individuals control wheelchair movement using simple hand gestures.

The system utilizes Computer Vision and Artificial Intelligence to recognize hand gestures in real-time through a webcam. Recognized gestures are translated into movement commands and transmitted to a wheelchair control system using serial communication.

The project aims to provide an intuitive, touch-free, and accessible mobility solution for users with limited physical capabilities.

---

## Problem Statement

Traditional wheelchairs require physical interaction through joysticks or manual controls, which may be difficult for individuals with severe motor impairments.

This project introduces a contactless gesture-based control system that enables wheelchair navigation through natural hand movements.

---

## Features

### Real-Time Hand Tracking

* Live webcam-based gesture detection
* Single-hand tracking
* Real-time landmark extraction

### Gesture Recognition

* Finger counting algorithm
* Dynamic gesture interpretation
* Instant command generation

### Wheelchair Navigation Commands

| Fingers Detected | Command  |
| ---------------- | -------- |
| 1 Finger         | Forward  |
| 2 Fingers        | Backward |
| 3 Fingers        | Right    |
| 4 Fingers        | Left     |
| 5 Fingers        | Stop     |

### Assistive Technology

* Designed for disabled persons
* Touch-free operation
* Low-cost implementation

### Desktop Application

* PyQt5 Graphical User Interface
* Login Authentication System
* Interactive Dashboard
* Easy-to-use controls

### Hardware Integration

* Arduino Communication
* Serial Port Control
* Wheelchair Motor Control Support

---

## System Architecture

User Hand Gesture
↓
Webcam Input
↓
OpenCV Video Processing
↓
MediaPipe Hand Landmark Detection
↓
Finger Counting Algorithm
↓
Gesture Classification
↓
Command Generation
↓
Serial Communication
↓
Arduino Controller
↓
Wheelchair Movement

---

## Technologies Used

### Artificial Intelligence

* Computer Vision
* Gesture Recognition
* Human-Computer Interaction

### Programming Languages

* Python

### Frameworks & Libraries

* PyQt5
* OpenCV
* MediaPipe
* PySerial

### Hardware

* Arduino Uno
* DC Motors
* Motor Driver
* Webcam

---

## Project Modules

### User Authentication Module

* Secure login interface
* User validation
* Dashboard navigation

### Hand Detection Module

* Real-time webcam capture
* Hand landmark extraction
* Finger position analysis

### Gesture Recognition Module

* Finger counting
* Command mapping
* Movement classification

### Communication Module

* Serial communication
* Arduino interfacing
* Command transmission

### Wheelchair Control Module

* Forward movement
* Backward movement
* Left turn
* Right turn
* Stop operation

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/hand-gesture-wheelchair.git
cd hand-gesture-wheelchair
```

### Install Dependencies

```bash
pip install opencv-python
pip install mediapipe
pip install pyqt5
pip install pyserial
```

### Run Application

```bash
python main.py
```

---

## Workflow

1. Launch application.
2. Login using credentials.
3. Open gesture control panel.
4. Start webcam.
5. Show hand gesture.
6. System detects fingers.
7. Corresponding command is generated.
8. Command is sent to Arduino.
9. Wheelchair moves accordingly.

---

## Applications

* Smart Wheelchairs
* Assistive Healthcare Systems
* Elderly Care Solutions
* Human Computer Interaction
* Gesture-Based Robotics
* Smart Mobility Systems

---

## Future Enhancements

* Deep Learning-Based Gesture Recognition
* Voice Command Integration
* Mobile Application Support
* Emergency Alert System
* Obstacle Detection
* IoT Monitoring Dashboard
* AI-Powered Navigation Assistance
* Face Recognition Authentication

---

## Skills Demonstrated

* Computer Vision
* OpenCV
* MediaPipe
* Human Computer Interaction
* Embedded Systems
* Arduino Programming
* Serial Communication
* PyQt5 GUI Development
* AI for Healthcare
* Assistive Technology Development

---

## Research Domain

* Artificial Intelligence
* Healthcare Technology
* Human Computer Interaction
* Smart Mobility Systems
* Computer Vision
* Embedded Systems

---

## Author

Suriya V

Computer Science Engineer | AI & Machine Learning Enthusiast

Specializations:

* Artificial Intelligence
* Machine Learning
* Computer Vision
* Assistive Technology
* Embedded AI Systems
