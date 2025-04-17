Okay, here's a comprehensive README file for your GitHub repository based on the Python code provided.

# Real-Time Face Recognition Attendance System using OpenCV and Firebase

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![OpenCV](https://img.shields.io/badge/opencv-4.x-green.svg)
![Firebase](https://img.shields.io/badge/firebase-Admin_SDK-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg) <!-- Choose a license -->

This project implements a real-time attendance system using face recognition. It leverages OpenCV for video capture and processing, the `face_recognition` library for detecting and identifying faces, and Google Firebase (Realtime Database and Cloud Storage) for data persistence and management.

## Features

*   **Real-Time Face Detection & Recognition:** Detects faces from a live webcam feed and identifies known individuals.
*   **Firebase Integration:**
    *   Stores student metadata (ID, Name, Major, etc.) in Firebase Realtime Database.
    *   Stores student images in Firebase Cloud Storage.
    *   Updates attendance count and last attendance time in real-time.
*   **Encoding Generation:** Generates and saves facial encodings locally for fast comparisons.
*   **Attendance Logic:** Marks attendance and prevents immediate re-marking using a time threshold (cooldown period).
*   **Visual Feedback:** Displays the live camera feed, highlights recognized faces, shows student information, and indicates system status using mode images.



## Project Structure


.
├── Main.py # Main script to run the attendance system
├── EncodeGenerator.py # Script to generate face encodings and upload images
├── AddDatatoDatabase.py # Script to add initial student data to Firebase DB
├── EncodeFile.p # Generated file containing known face encodings and IDs
├── serviceAccountKey.json # Firebase Admin SDK credentials (DO NOT COMMIT TO PUBLIC REPOS)
├── Resources/ # Folder for UI assets
│ ├── background.png # Background image for the UI
│ └── Modes/ # Folder containing UI mode images (e.g., 1.png, 2.png, 3.png, 4.png)
├── Images/ # Folder containing student images (e.g., 321654.png)
├── requirements.txt # List of Python dependencies
└── README.md # This file

## Prerequisites

1.  **Python:** Version 3.7.6 recommended.
2.  **Firebase Project:**
    *   Create a project on the [Firebase Console](https://console.firebase.google.com/).
    *   Enable **Realtime Database**.
    *   Enable **Cloud Storage**.
3.  **Firebase Admin SDK Key:**
    *   In your Firebase project settings, go to "Service accounts".
    *   Click "Generate new private key" and download the `.json` file.
    *   Rename this file to `serviceAccountKey.json` and place it in the project's root directory.
    *   **IMPORTANT:** Add `serviceAccountKey.json` to your `.gitignore` file to prevent accidentally committing sensitive credentials to version control.
4.  **Webcam:** A functional webcam connected to your computer.
5.  **Student Images:** Collect images of the students/individuals you want to enroll. Name each image file with the corresponding student ID (e.g., `321654.png`, `852741.png`). Place these images inside the `Images` folder.
6.  **Resource Files:** Ensure the `Resources` folder contains `background.png` and a `Modes` subfolder with numbered images (`1.png`, `2.png`, etc.) representing different UI states (Active, Loading, Marked, Already Marked).

## Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(See `requirements.txt` content below)*

3.  **Configure Firebase:**
    *   Open `Main.py`, `EncodeGenerator.py`, and `AddDatatoDatabase.py`.
    *   Find the lines initializing Firebase:
        ```python
        firebase_admin.initialize_app(cred, {
            'databaseURL': "YOUR_DATABASE_URL_HERE",  # Replace
            'storageBucket': "YOUR_STORAGE_BUCKET_URL_HERE" # Replace (e.g., your-project-id.appspot.com)
        })
        ```
    *   Replace `"YOUR_DATABASE_URL_HERE"` with your Firebase Realtime Database URL.
    *   Replace `"YOUR_STORAGE_BUCKET_URL_HERE"` with your Firebase Storage bucket URL (usually `your-project-id.appspot.com`).
    *   Ensure `serviceAccountKey.json` is in the root directory.

4.  **Prepare Images:**
    *   Place your collected student images (named `StudentID.png` or similar - ensure consistency with `EncodeGenerator.py`) into the `Images/` folder.

5.  **Prepare Resources:**
    *   Ensure the `Resources/` folder and its contents (`background.png`, `Modes/1.png`, etc.) are present.

6.  **Add Initial Student Data to Firebase:**
    *   Modify the `data` dictionary in `AddDatatoDatabase.py` with your actual student information, matching the IDs used for image filenames.
    *   Run the script:
        ```bash
        python AddDatatoDatabase.py
        ```
    *   Verify the data appears in your Firebase Realtime Database console.

7.  **Generate Encodings and Upload Images:**
    *   Run the encoding generator script:
        ```bash
        python EncodeGenerator.py
        ```
    *   This will:
        *   Read images from the `Images/` folder.
        *   Generate face encodings.
        *   Save encodings and IDs to `EncodeFile.p`.
        *   Upload the images from `Images/` to your Firebase Storage bucket under the `Images/` path.
    *   Verify the `EncodeFile.p` is created and images appear in Firebase Storage.

## Usage

1.  **Run the Main Application:**
    ```bash
    python Main.py
    ```
2.  The application window should appear, showing the live webcam feed overlaid on the background.
3.  When a known face is detected and recognized:
    *   A bounding box will appear around the face.
    *   The system will fetch student data from Firebase.
    *   Student details and their image (from Firebase Storage) will be displayed.
    *   Attendance will be marked (if the cooldown period has passed), updating Firebase.
    *   Status messages ("Loading", "Marked", "Already Marked") will be shown in the UI.

## Configuration

*   **Firebase Credentials:** `serviceAccountKey.json` (required).
*   **Firebase URLs:** Must be set correctly in `Main.py`, `EncodeGenerator.py`, and `AddDatatoDatabase.py`.
*   **Image Naming:** Images in `Images/` folder must be named `StudentID.extension` (matching IDs in `AddDatatoDatabase.py`).
*   **Resource Paths:** The code assumes `Resources/` and `Images/` folders are in the same directory as the scripts.
*   **Attendance Cooldown:** The time threshold (in seconds) before marking attendance again can be modified in `Main.py` (variable `secondsElapsed > 30`).
*   **Camera Index:** `cv2.VideoCapture(1)` uses the second camera detected. Change to `0` for the default camera if needed.

## Dependencies (`requirements.txt`)

```txt
opencv-python
face_recognition
firebase-admin
numpy
cvzone
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
IGNORE_WHEN_COPYING_END
Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

License

Distributed under the MIT License. See LICENSE file for more information. (You should create a LICENSE file, e.g., containing the MIT License text)

Acknowledgements

face_recognition library by Adam Geitgey

OpenCV

Firebase

cvzone library by Computer Vision Zone

**To make this complete:**

1.  **Replace Placeholders:** Update `your-username/your-repo-name` and any other specific placeholders.
2.  **Choose a License:** Select a license (MIT is a common choice for open source) and create a `LICENSE` file in your repository containing the license text. Update the badge and license section if you choose something other than MIT.
3.  **Create `requirements.txt`:** Create a file named `requirements.txt` and paste the dependencies list into it.
4.  **Add `.gitignore`:** Create a `.gitignore` file and add `serviceAccountKey.json` and potentially other files/folders like `__pycache__/`, `*.pyc`, `EncodeFile.p` to it.
    ```gitignore
    # Firebase credentials
    serviceAccountKey.json

    # Python cache
    __pycache__/
    *.pyc

    # Generated files
    EncodeFile.p

    # Environment folders (if used)
    venv/
    .venv/
    ```
