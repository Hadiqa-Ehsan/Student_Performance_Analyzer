
# 🎓 Student Performance Analyzer

A Python tool to track student grades, analyze academic performance, and generate progress reports for teachers and parents.

## ✨ Features

- **Student Data Input** – Add student names, grades, and subjects
- **Grade Tracking** – Record scores for multiple subjects and exams
- **Average Calculation** – Calculate subject-wise and overall averages
- **Grade Classification** – Assign A, B, C, D, or F grades based on scores
- **Class Ranking** – Rank students by overall performance
- **Subject-wise Analysis** – Identify strong and weak subjects
- **Progress Reports** – Generate individual student report cards
- **CSV Export** – Save data for record keeping

## 🛠️ Technologies Used

- **Python 3.x**
- **Pandas** – Data manipulation and analysis
- **Statistics Module** – Mean, median, and standard deviation
- **CSV Module** – Data storage

## 📁 Project Structure

```
Student_Performance_Analyzer/
├── student_analyzer.py   # Main program
├── student_data.csv      # Stored student records
├── report_card.csv       # Generated reports
└── README.md             # Documentation
```

## 🔧 How to Run

1. Download or clone the project
2. Open terminal in the project folder
3. Install dependencies:

```bash
pip install pandas
```

4. Run the program:

```bash
python student_analyzer.py
```

## 📖 Usage Example

```
--- Student Performance Analyzer ---

1. Add Student
2. Add Grades
3. View Class Report
4. Generate Report Card
5. View Class Ranking
6. Exit

Enter your choice: 1
Enter student name: Ali Raza
Enter grade level: 10
Enter section: A

Student added successfully!

Enter choice: 2
Select student: Ali Raza
Enter subject name: Mathematics
Enter marks (0-100): 85
Enter subject name: Science
Enter marks (0-100): 78
Enter subject name: English
Enter marks (0-100): 92
Enter subject name: done

Grades recorded!

Enter choice: 3
--- Class Performance Report ---
Total Students: 25
Class Average: 79.4
Highest Score: 96 (Fatima Khan)
Lowest Score: 58 (Hamza Ali)
```

## 📊 Grade Scale

| Marks Range | Grade | Status |
|-------------|-------|--------|
| 90 - 100 | A+ | Excellent |
| 80 - 89 | A | Very Good |
| 70 - 79 | B | Good |
| 60 - 69 | C | Satisfactory |
| 50 - 59 | D | Needs Improvement |
| Below 50 | F | Fail |

## 📋 Sample Report Card

```
=====================================
         REPORT CARD
=====================================
Student Name: Ali Raza
Grade: 10 - Section A
=====================================
Subject         Marks    Grade
Mathematics     85       A
Science         78       B
English         92       A+
Computer        81       A
-------------------------------------
Total: 336 / 400
Percentage: 84.0%
Overall Grade: A
Status: PASS ✓
=====================================
```

## 📌 Future Improvements

- Add attendance tracking
- Visual charts with matplotlib
- Parent/guardian notification system
- Subject-wise improvement suggestions
- Generate PDF reports instead of CSV

## 👩‍💻 Author

**Hadiqa Ehsan**  
[GitHub Profile](https://github.com/Hadiqa-Ehsan)

## 📄 License

MIT License

---

⭐ Star this repo if you found it useful for educational analytics!
