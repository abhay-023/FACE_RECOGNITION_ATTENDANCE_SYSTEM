🎓 Smart Attendance Management System using Face Recognition
An AI-based attendance system that uses face recognition to automatically mark student attendance through a webcam. This project replaces manual attendance with a fast, contactless, and secure digital solution.

📌 Features
🎥 Real-time face detection using webcam
🧠 Face recognition using AI-based encodings
📝 Automatic attendance marking with date & time
👤 Student face registration system
🌐 Simple web interface using Flask

📁 Attendance stored in CSV format
🛠 Technologies Used
Technology	Purpose
Python	Core programming language
Flask	Web framework (backend)
OpenCV	Webcam access & image processing
face_recognition	Face detection & recognition
NumPy	Numerical operations
Pandas	Attendance data handling
HTML/CSS	Frontend design
JavaScript	Web interactivity

📂 Project Structure
Smart_Attendance_System/
│
├── app.py                  # Main backend application
├── requirements.txt        # Required libraries
├── attendance.csv          # Attendance records
│
├── known_faces/            # Stored student face images
│
├── templates/
│   ├── index.html          # Home page
│   └── register.html       # Student registration page
│
└── static/
    └── style.css           # Styling for web pages

⚙️ How the System Works
Students register their face through the webcam
The system stores the face image and generates a face encoding
During attendance, live video is captured
Faces are detected and matched with stored encodings
If a match is found, attendance is recorded with date & time

💻 Installation & Setup Guide
1️⃣ Install Python
Download and install Python (3.8 or above) from the official website.
2️⃣ Create Project Folder
Create a folder on Desktop:
Smart_Attendance_System
Add the project files and folders inside it as shown in the structure above.
3️⃣ Install Required Libraries
Open terminal / command prompt inside the project folder and run:
pip install flask opencv-python face-recognition numpy pandas
4️⃣ Run the Application
In the project folder, run:
python app.py

You will see:
Running on http://127.0.0.1:5000/
Open this link in your browser.

🧑‍💻 How to Use
🔹 Register Student
Go to Register page
Enter student name
Face will be captured and saved
🔹 Mark Attendance
Click Start Attendance
System recognizes faces and marks attendance automatically

📊 Attendance Format
Attendance is saved in attendance.csv like this:
Name,Time,Date
Rahul,09:10:23,29-01-2026
Anita,09:11:02,29-01-2026

✅ Advantages
Contactless system
Prevents proxy attendance
Saves time
Easy to use
Low cost

⚠️ Limitations
Needs good lighting
Accuracy depends on camera quality
Face changes (mask, glasses) may reduce accuracy

🚀 Future Improvements
Database integration (MySQL)
Admin dashboard
Cloud-based system
Mobile app support
SMS/Email alerts

👨‍🎓 Author
Abhay Singh
Smart Attendance System Project
