
import pandas as pd
import numpy as np

# Load the student dataset
df = pd.read_csv("students.csv")

# Display the first five records
print("FIRST FIVE STUDENT RECORDS")
print(df.head())

# Display the column names
print("\nDATASET COLUMNS")
print(df.columns.tolist())

# Display the number of records and columns
print("\nDATASET SHAPE")
print(df.shape)

# Display dataset information
print("\nDATASET INFORMATION")
df.info()


# Calculate total marks for each student
df["Total_Marks"] = df["Python"] + df["SQL"] + df["Statistics"]

# Calculate average marks for each student
df["Average_Marks"] = df["Total_Marks"] / 3

# Display student marks summary
print("\nSTUDENT MARKS SUMMARY")
print(df[["Student_ID", "Name", "Total_Marks", "Average_Marks"]].to_string(index=False))


# Assign grades based on average marks
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 50:
        return "E"
    else:
        return "F"


# Determine pass or fail

# Determine pass or fail
def calculate_result(row):
    if (
        row["Python"] >= 40
        and row["SQL"] >= 40
        and row["Statistics"] >= 40
        and row["Average_Marks"] >= 50
    ):
        return "Pass"
    else:
        return "Fail"


# Apply the functions to every student
df["Grade"] = df["Average_Marks"].apply(calculate_grade)
df["Result"] = df.apply(calculate_result, axis=1)

# Display grades and results
print("\nSTUDENT GRADES AND RESULTS")
print(
    df[["Student_ID", "Name", "Average_Marks", "Grade", "Result"]]
    .to_string(index=False, formatters={"Average_Marks": "{:.2f}".format})
)


# STUDENT PERFORMANCE ANALYSIS

# Find the student with the highest average
highest_average = df["Average_Marks"].max()
top_students = df[df["Average_Marks"] == highest_average]

print("\nTOP-PERFORMING STUDENT(S)")
print(
    top_students[["Student_ID", "Name", "Average_Marks"]]
    .to_string(index=False, formatters={"Average_Marks": "{:.2f}".format})
)

# Find the student with the lowest average
lowest_average = df["Average_Marks"].min()
lowest_students = df[df["Average_Marks"] == lowest_average]

print("\nLOWEST-PERFORMING STUDENT(S)")
print(
    lowest_students[["Student_ID", "Name", "Average_Marks"]]
    .to_string(index=False, formatters={"Average_Marks": "{:.2f}".format})
)

# Calculate subject-wise averages
subject_averages = df[["Python", "SQL", "Statistics"]].mean()

print("\nSUBJECT-WISE AVERAGE MARKS")
print(subject_averages.round(2))

# Find the subject with the highest average
best_subject = subject_averages.idxmax()
print("\nBEST-PERFORMING SUBJECT:", best_subject)

# Calculate the overall class average using NumPy
class_average = np.mean(df["Average_Marks"])
print(f"OVERALL CLASS AVERAGE: {class_average:.2f}")

# Count pass and fail students
pass_count = (df["Result"] == "Pass").sum()
fail_count = (df["Result"] == "Fail").sum()

print("\nPASS/FAIL SUMMARY")
print("Students Passed:", pass_count)
print("Students Failed:", fail_count)


# DEPARTMENT-WISE PERFORMANCE ANALYSIS

# Calculate average marks and attendance by department
department_analysis = df.groupby("Department").agg(
    Student_Count=("Student_ID", "count"),
    Average_Marks=("Average_Marks", "mean"),
    Average_Attendance=("Attendance", "mean")
)

print("\nDEPARTMENT-WISE PERFORMANCE")
print(department_analysis.round(2))

# Find the department with the highest average marks
best_department = department_analysis["Average_Marks"].idxmax()
best_department_average = department_analysis.loc[
    best_department, "Average_Marks"
]

print("\nBEST-PERFORMING DEPARTMENT:", best_department)
print(f"DEPARTMENT AVERAGE: {best_department_average:.2f}")


# TOP FIVE STUDENTS

top_five_students = df.sort_values(
    by="Average_Marks",
    ascending=False
).head(5)

print("\nTOP FIVE STUDENTS")
print(
    top_five_students[
        ["Student_ID", "Name", "Department", "Average_Marks", "Grade"]
    ].to_string(
        index=False,
        formatters={"Average_Marks": "{:.2f}".format}
    )
)


# FINAL PROJECT REPORT

print("\n" + "=" * 45)
print(" STUDENT PERFORMANCE ANALYTICS REPORT")
print("=" * 45)

print(f"Total students analyzed : {len(df)}")
print(f"Overall class average   : {class_average:.2f}")
print(f"Students passed         : {pass_count}")
print(f"Students failed         : {fail_count}")
print(f"Best-performing subject : {best_subject}")
print(f"Best-performing dept.   : {best_department}")
print(f"Top student             : {top_students.iloc[0]['Name']}")
print(f"Top student average     : {highest_average:.2f}")

print("=" * 45)
print("REPORT GENERATED SUCCESSFULLY")
print("=" * 45)