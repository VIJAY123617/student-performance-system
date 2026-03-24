import pyodbc

conn = pyodbc.connect(
    'DRIVER={SQL SERVER};'
    'SERVER=DESKTOP-1V0CTHE\\SQLEXPRESS02;'
    'DATABASE=student_db;'
    'TRUSTED_CONNECTION=YES;'
)
cursor= conn.cursor()

  #Menu loop
while True:
    print("\n===||| STUDENT PERFORMANCE ANALYSIS SYSTEM |||===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Topper (Mark & Attendance)")
    print("7. Course Average")
    print("8. Export to Excel")
    print("0. Exit")

    choice = input("Enter your choice:").strip()

    # ➕ Add Student
    if choice == '1':
        while True:
                id = int(input("Enter ID: "))
               # ID checker..
                cursor.execute("SELECT * FROM student WHERE ID=?",(id,))
                if cursor.fetchone():
                      print("❌ ID already exists! Enter a unique ID.\n")
                else:
                    break    
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        mark = int(input("Enter Marks: "))
        
        while True:
              attendance =int(input("Enter Attendance(35-99): "))
              if 35 <= attendance <=99:
                break 
              else:
                print("❌ invalid Attendance please insert 35 to 99")   

        cursor.execute(
        "INSERT INTO student VALUES (?, ?, ?, ?, ?)",
                (id, name, course, mark, attendance))
                  
        conn.commit()
        print("Student Added Successfully✅")

    # 📊 View Students
    elif choice == '2':
        cursor.execute("SELECT * FROM student")
        rows=cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print(("No records found ❌") )        
             
    # ✏️ Update......
    elif choice == '3':
        id = int(input("Enter ID: "))
        mark = int(input("Enter new marks: "))
        while True:
            attendance =int(input("Enter new attendance(35-99): "))
            if 35<= attendance <=99:
                break
            else:
                print("❌ invalid Attendance please insert 35 to 99")
               
                

        cursor.execute(
            "UPDATE student SET MARK=?, ATTENDANCE=? WHERE ID=?",
            (mark, attendance, id)
        )
        conn.commit()
        print("Updated ✅")

    # ❌ Delete
    elif choice == '4':
        id = int(input("Enter ID: "))

        cursor.execute("DELETE FROM student WHERE ID=?", (id,))
        conn.commit()
        print("Deleted ✅")

    #  Search
    elif choice == '5':
        id = int(input("Enter ID: "))

        cursor.execute("SELECT * FROM student WHERE ID=?", (id,))
        data = cursor.fetchone()

        if data:
            print(data)
        else:
            print("Not found ❌")

    # 🏆 Topper
    elif choice == '6':
        cursor.execute("""SELECT TOP 1 *,
ROUND(mark * 0.8 + attendance * 0.2, 2) AS score
FROM student
ORDER BY score DESC;""")
        print("Topper:", cursor.fetchone())

    #  Course Average
    elif choice == '7':
        cursor.execute("""
        SELECT COURSE, AVG(MARK)
        FROM student
        GROUP BY COURSE
        """)
        for row in cursor.fetchall():
         print(row)

    #  Excel Export
    elif choice == '8':
        import pandas as pd
        df = pd.read_sql("SELECT * FROM student", conn)
        df.to_excel("students.xlsx", index=False)
        print("Excel Created ✅")
        
  #  Exit
    elif choice == '0':
        print("Exiting...")
        break
    else:
        print("Invalid choice ❌")