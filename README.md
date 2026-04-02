# Employee Attendance Management System (Face Recognition)

## Project Type

---

## Problem Statement

Many organizations and institutions still use manual attendance systems, which are time-consuming and prone to errors such as proxy attendance and incorrect records.
This project aims to develop an automated attendance system using **Machine Learning and Face Recognition** to accurately mark attendance and store it digitally. The system detects and recognizes faces through a webcam and automatically records attendance with date and time.

---

## My Contribution

* Collected and preprocessed student face image dataset
* Implemented face detection using OpenCV
* Implemented face recognition using LBPH algorithm
* Developed Python GUI for system interface
* Integrated database for attendance storage
* Testing, debugging, and documentation

---

## Algorithms Used

* Haar Cascade Classifier (Face Detection)
* LBPH – Local Binary Pattern Histogram (Face Recognition)
* Image Processing using OpenCV

---

## Project Structure

```
Attendance-Management-System/
│
├── dataset/                         # Student images
├── trainer/                         # Trained model
├── attendance/                      # Attendance records
├── haarcascade_frontalface_default.xml
├── train.py                         # Train model
├── recognize.py                     # Recognize face & mark attendance
├── student.py                       # Add student details
├── attendance.py                    # Attendance management
├── main.py                          # Main GUI
└── README.md
```

---

## Tech Stack

* Python
* OpenCV
* NumPy
* Pandas
* Scikit-learn
* Tkinter (GUI)
* SQLite (Database)

---

## How To Run

1. Install dependencies

```
pip install opencv-python numpy pandas scikit-learn pillow
```

2. Run the project

```
python main.py
```

3. First add student images → Train model → Run face recognition → Attendance will be marked automatically.

---

## Output

* The system captures face through webcam
* Recognizes the student
* Marks attendance with date and time
* Stores attendance in database/CSV file

---

## Future Improvements

* Mask face recognition
* Mobile app integration
* Cloud database
* Email notification for attendance
* Admin login system

---

If your teacher asks **“Why LBPH?”** in viva, answer:

> LBPH is used because it is fast, works well on small datasets, and is suitable for real-time face recognition systems.

---

If you want, I can also make:

* requirements.txt
* Flowchart
* Viva questions & answers
