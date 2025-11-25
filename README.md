📄 CSV Reader — Python CLI Tool

A simple and feature-rich CSV Student Marks Reader created in Python.
This tool reads a CSV file containing student names and marks, and allows you to perform multiple operations such as:

🔹 View list of passed students

🔹 Calculate percentage of passed students

🔹 View topper(s) (supports multiple toppers)

🔹 Terminal-friendly clean output

🔹 Fully menu-driven CLI interface

This repository is ideal for learning Python fundamentals, CSV handling, and making neat terminal tools.

📁 CSV Format

Your .csv file must follow this simple structure:
```
Name,Marks
Rafay,42
Eman,91
Hassan,27
Kiran,63
Zoya,15
Talha,84
```

First column → Student Name
Second column → Marks (integer)

No extra spaces, quotes, or headers needed.

🚀 Features
✔ 1. Percentage Calculator (.percentage)

Calculates what percentage of students have passed based on the passing marks criteria (default: 50).

Example output:
```
------------------------------------
65% students passed.
------------------------------------
```
✔ 2. Topper Finder (.topper)

Shows the student(s) with the highest marks.
Supports multiple toppers (if multiple students share the same highest marks).

Example:
```
==========================================================
Sarim with the score of 98 is topper
Haider with the score of 98 is topper
==========================================================
```
✔ 3. Pass List (.passlist)

Displays all passed students along with their marks.
```
------------------------------
=> Passed Students :
------------------------------
• Kiran | Marks: 63
• Talha | Marks: 84
• Eman  | Marks: 91
------------------------------
```
🛠 How It Works

You start the script, provide the CSV file path, and then choose what task to perform.
```
• File to Locate (.csv) : students.csv
 What task to Perform ? : .topper
```

The script then processes and displays output in a clean terminal-friendly format.

⚙ Commands List
Command	Description
.percentage	Shows percentage of passed students
.topper	Displays student(s) with the highest marks
.passlist	Lists all passed students with their marks

📌 Configuration
Change Passing Marks
Modify this line in the code:
```
passing_marks = 50
```
You may also adjust:
```
total_marks = 100
```
depending on your grading system.

📦 Requirements

This project uses only Python’s built-in modules, so no external libraries are needed.
```
Python 3.x
CSV file to load
```
▶ Running the Script

Clone the repo:
```
git clone https://github.com/yourusername/csv-reader.git
cd csv-reader
```

Run:
```
python CSVreader.py
```

Follow the on-screen prompts.

📚 Code Structure
main.py
├── CSV reading and parsing
├── percentage_of_passed()
├── passlist() and decorators
├── topper finder logic
└── main input loop


Functions are cleanly separated for easy modification and extension.
