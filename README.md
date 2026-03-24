
# Student Performance Analysis System

A Python-based application integrated with SQL Server to manage and analyze student performance data. This system helps in storing, updating, and analyzing student records efficiently with useful insights.
## 🚀 Features

- ➕ Add new student records with validation  
- 📋 View all student data  
- ✏️ Update student marks and attendance  
- ❌ Delete student records  
- 🔍 Search student by ID  
- 🏆 Identify topper based on performance score  
- 📊 Calculate course-wise average marks  
- 📁 Export student data to Excel  

---

## 🛠️ Technologies Used

- Python  
- SQL Server  
- pyodbc  
- Pandas  
- Excel  

---

## 📂 Project Structure
Student-Performance-System/
│
├── Student_Analysis_System.py
├── README.md
└── students.xlsx


---

### 2️⃣ Create Database in SQL Server

CREATE DATABASE student_db;

USE student_db;

CREATE TABLE student (
    ID INT PRIMARY KEY,
    NAME VARCHAR(50),
    COURSE VARCHAR(50),
    MARK INT,
    ATTENDANCE INT
);

Configure Database Connection

Update your connection string in Python:

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=YOUR_SERVER_NAME;'
    'DATABASE=student_db;'
    'TRUSTED_CONNECTION=YES;'
)

#Run the Project
python Student_Analysis_System.py
📈 Performance Calculation
Topper is calculated using the following formula:

Score = (Marks * 0.8) + (Attendance * 0.2)

✅ Validation Rules
Marks must be between 0–100
Attendance must be between 35–100
Student ID must be unique

#Sample Output
Topper: (101, 'Rahul', 'BCA', 92, 95, 93.6)

 Future Enhancements
GUI using Tkinter or Web App using Flask
User Authentication System
Data Visualization (Charts & Graphs)
API Integration
👨‍💻 Author

Vijay Dubey
Data Analyst || python | SQL | Data Analysis


Support

If you like this project, please give it a ⭐ on GitHub!
