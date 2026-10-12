# Student Performance Analytics System

## 1. Project Title and Student Details

**Project Title:** Student Performance Analytics System
**Student Name:** Lingaswamy
**Technologies:** Python, Pandas, NumPy
**GitHub Repository:** https://github.com/Lingaswamy727/student-performance-analytics

## 2. Objective

The objective of this project is to develop a Python-based Student Performance Analytics System that processes student academic data and generates meaningful performance reports.

The system calculates total and average marks, assigns grades, identifies pass and fail results, analyzes subject-wise performance, compares departments, and identifies top-performing and lowest-performing students.

## 3. Technologies Used

* **Python:** Implements the program logic, functions, conditions, and calculations.
* **Pandas:** Loads the CSV dataset, organizes records in a DataFrame, and performs data analysis.
* **NumPy:** Performs numerical calculations, including the overall class average.
* **CSV:** Stores the student dataset.
* **Git and GitHub:** Manage project versions and host the source code online.
* **Visual Studio Code with WSL Ubuntu:** Used to develop and run the project.

## 4. Dataset Description

The project uses a CSV dataset named `students.csv`.

The dataset contains 20 student records and 7 columns:

| Column     | Description                   |
| ---------- | ----------------------------- |
| Student_ID | Unique student identifier     |
| Name       | Student name                  |
| Department | Student's department          |
| Python     | Python subject marks          |
| SQL        | SQL subject marks             |
| Statistics | Statistics subject marks      |
| Attendance | Student attendance percentage |

Pandas is used to load the dataset and inspect its columns, dimensions, and data types.

## 5. Implementation

### Step 1: Load the dataset

The program reads `students.csv` using Pandas and displays the first five records.

### Step 2: Inspect the data

The program displays the column names, dataset shape, and basic DataFrame information.

### Step 3: Calculate total and average marks

The program calculates each student's total marks across Python, SQL, and Statistics. It then calculates average marks across the three subjects.

### Step 4: Assign grades

The program uses a reusable function to assign grades based on average marks:

* A: 90 and above
* B: 80 to below 90
* C: 70 to below 80
* D: 60 to below 70
* E: 50 to below 60
* F: Below 50

### Step 5: Determine pass or fail

A student passes when all three subject marks are at least 40 and the average marks are at least 50. Otherwise, the student fails.

### Step 6: Analyze performance

The program identifies the highest- and lowest-performing students, calculates subject-wise averages, determines the overall class average, and counts students who passed and failed.

### Step 7: Analyze departments and top performers

The program groups students by department to calculate student counts, average marks, and average attendance. It also displays the top five students.

### Step 8: Generate the final report

The program summarizes the key results in a readable report and displays a success message after completing the analysis.

## 6. Key Features

* Loads and analyzes a 20-record student dataset.
* Calculates total and average marks.
* Assigns grades using defined conditions.
* Determines pass/fail status.
* Identifies the highest- and lowest-performing students.
* Calculates subject-wise averages.
* Computes the overall class average using NumPy.
* Summarizes department-wise marks and attendance.
* Displays the top five students.
* Generates a final performance report.

## 7. Output and Screenshots

The program was executed successfully in the WSL Ubuntu terminal.

The following screenshots demonstrate the output:

1. Dataset information and student marks summary.
2. Student grades and pass/fail results.
3. Subject averages and department-wise performance.
4. Top five students and final analytics report.

The screenshots should be included with the project documentation or in a clearly named screenshots folder, according to the submission requirements.

## 8. Final Outcome

The Student Performance Analytics System successfully analyzed 20 student records.

The final results were:

* Total students analyzed: 20
* Overall class average: 73.08
* Students passed: 17
* Students failed: 3
* Best-performing subject: SQL
* Best-performing department: ECE
* Department average for ECE: 80.56
* Top-performing student: Harini
* Top student's average: 96.33
* Lowest-performing student: Kiran
* Lowest student's average: 38.33

The program displayed `REPORT GENERATED SUCCESSFULLY` after completing the analysis.

## 9. Challenges and Learning

During this project, I practiced organizing a Python project, setting up a virtual environment, installing libraries, loading CSV data, and analyzing records with Pandas and NumPy.

I learned how to write reusable functions, apply conditional logic for grades and pass/fail results, group data by department, calculate averages, and present results in a structured report.

I also practiced Git commands for initializing a repository, staging files, creating commits, connecting to GitHub, and pushing the project online.

This project improved my understanding of Python fundamentals and practical data analysis.

## 10. GitHub Repository

**Repository URL:** https://github.com/Lingaswamy727/student-performance-analytics

The repository contains the Python program, CSV dataset, requirements file, README, and project documentation.

**Project Status:** Implemented, tested, and published to GitHub.
