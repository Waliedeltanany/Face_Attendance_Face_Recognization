# Face Recognition Attendance System

## 📌 Project Overview

This project is a **Face Recognition–Based Attendance System** built using **Python**. It provides a graphical user interface (GUI) that allows users to **log in**, **log out**, and **register new users** using real-time face recognition through a webcam.

The system is designed as a **team project (5 members)** and follows proper GitHub collaboration practices for academic submission.

---

## 🎯 Project Objectives

* Automate attendance using face recognition
* Eliminate manual sign-in/sign-out processes
* Provide a simple and interactive GUI
* Log user entry and exit times automatically

---

## 🧠 How the System Works

1. The webcam captures the user's face in real time.
2. Face embeddings are extracted using **DeepFace (FaceNet model)**.
3. The captured face is compared with stored faces using **cosine similarity**.
4. If a match is found:

   * User can **log in** or **log out**
   * The action is saved in a log file with timestamp
5. New users can register by capturing their face and saving it to the database.

---

## 🖥️ Features

* Real-time webcam face detection
* Face recognition using DeepFace
* User registration with face capture
* Login / Logout system
* Automatic attendance logging
* Simple and clean GUI using Tkinter

---

## 🛠️ Technologies Used

* **Python 3.9+**
* **Tkinter** (GUI)
* **OpenCV** (Webcam handling)
* **DeepFace** (Face recognition)
* **NumPy** (Numerical computations)
* **Pillow (PIL)** (Image processing)

---

## 📂 Project Structure

```
project-root/
│── main.py          # Main application (GUI & logic)
│── util.py          # Helper functions & face recognition logic
│── db/
│   └── known/       # Stored images of registered users
│── log.txt          # Login/Logout records
│── README.md        # Project documentation
```

---

## ▶️ How to Run the Project

### 1️⃣ Install Required Libraries

```bash
pip install opencv-python deepface numpy pillow
```

### 2️⃣ Run the Application

```bash
python main.py
```

---

## 🧪 Usage Instructions

* **Register New User**:

  * Click `register new user`
  * Enter username
  * Capture face and save

* **Login**:

  * Click `login`
  * If face is recognized, login is recorded

* **Logout**:

  * Click `logout`
  * Logout time is recorded

---

## 📝 Attendance Log Format

All login and logout actions are saved in `log.txt` as:

```
username,YYYY-MM-DD HH:MM:SS,in
username,YYYY-MM-DD HH:MM:SS,out
```

---

## 👥 Team Members

This project was developed by a **team of 5 members**, where:

* Each member was responsible for specific modules or features
* GitHub commits reflect individual contributions

> *(Names can be added here before final submission)*

---

## ⚠️ Notes for Submission

* The project follows GitHub best practices
* No ZIP uploads — full commit history is available
* Each team member has identifiable contributions

---

## 📌 Future Improvements

* Add database support (SQLite / MySQL)
* Improve recognition accuracy
* Add admin panel
* Export attendance reports

---

## 📷 Disclaimer

* A working webcam is required
* Proper lighting improves recognition accuracy

---

✅ **This README is prepared for academic submission and GitHub evaluation.**
