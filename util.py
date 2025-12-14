import os
import numpy as np
import tkinter as tk
from tkinter import messagebox
from deepface import DeepFace

# ================= UI Helpers =================

def get_button(window, text, color, command, fg='white'):
    button = tk.Button(
        window,
        text=text,
        activebackground="black",
        activeforeground="white",
        fg=fg,
        bg=color,
        command=command,
        height=2,
        width=20,
        font=('Helvetica bold', 20)
    )
    return button

def get_img_label(window):
    label = tk.Label(window)
    label.grid(row=0, column=0)
    return label

def get_text_label(window, text):
    label = tk.Label(window, text=text)
    label.config(font=("sans-serif", 21), justify="left")
    return label

def get_entry_text(window):
    inputtxt = tk.Text(window, height=2, width=15, font=("Arial", 32))
    return inputtxt

def msg_box(title, description):
    messagebox.showinfo(title, description)

# ================= Face Recognition =================

def cosine_distance(a, b):
    return 1 - np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def recognize(img, db_path=None):
    """
    Recognize a face using images in db/known.
    img : numpy array (OpenCV image)
    db_path : folder containing known user images (.jpg/.png)
    """
    if db_path is None:
        db_path = os.path.join(os.getcwd(), "db", "known")

    if not os.path.exists(db_path):
        return 'unknown_person'

    try:
        reps_unknown = DeepFace.represent(
            img_path=img,
            model_name="Facenet",
            enforce_detection=False
        )
    except Exception:
        return 'no_persons_found'

    if len(reps_unknown) == 0:
        return 'no_persons_found'

    embedding_unknown = np.array(reps_unknown[0]["embedding"])
    threshold = 0.4
    match_name = None

    for file_name in os.listdir(db_path):
        if file_name.lower().endswith((".jpg", ".png")):
            file_path = os.path.join(db_path, file_name)
            try:
                reps_known = DeepFace.represent(
                    img_path=file_path,
                    model_name="Facenet",
                    enforce_detection=False
                )
                if len(reps_known) == 0:
                    continue
                embedding_known = np.array(reps_known[0]["embedding"])
            except Exception:
                continue

            distance = cosine_distance(embedding_known, embedding_unknown)
            if distance < threshold:
                match_name = os.path.splitext(file_name)[0]
                break

    if match_name:
        return match_name
    else:
        return 'unknown_person'
