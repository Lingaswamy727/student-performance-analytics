
# Student Performance Analytics System

## Project Overview
A Python-based project that analyzes student academic performance using Pandas and NumPy.

## Features
- Load student records from a CSV file
- Calculate total and average marks
- Assign grades and pass/fail results
- Identify the highest- and lowest-performing students
- Calculate subject-wise average marks
- Analyze performance by department
- Display the top five students
- Generate a final performance report

## Technologies Used
- Python
- Pandas
- NumPy
- CSV dataset

## Dataset
The dataset contains 20 student records with student IDs, names, departments, marks in Python, SQL and Statistics, and attendance.

## Pass/Fail Rules
A student passes if:
- Marks in each subject are at least 40
- Overall average marks are at least 50

Otherwise, the student fails.

## Grade Rules
| Average Marks | Grade |
|---|---|
| 90–100 | A |
| 80–less than 90 | B |
| 70–less than 80 | C |
| 60–less than 70 | D |
| 50–less than 60 | E |
| Below 50 | F |

## Installation and Execution

1. Clone or download this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   `pip install -r requirements.txt`

4. Run the application:

   `python main.py`

## Current Sample Results
- Students analyzed: 20
- Overall class average: 73.08
- Students passed: 17
- Students failed: 3
- Best-performing subject: SQL
- Best-performing department: ECE
- Top student: Harini, with an average of 96.33

## Author
Lingaswamy