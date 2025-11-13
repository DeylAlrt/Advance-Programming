import tkinter as tk
from tkinter import ttk, messagebox
import os

# Load student data
def load_students(filename):
    students = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
        total_students = int(lines[0])
        for line in lines[1:]:
            parts = line.split(",")
            student_code = int(parts[0])
            name = parts[1]
            course_marks = list(map(int, parts[2:5]))
            exam_mark = int(parts[5])
            students.append({
                "code": student_code,
                "name": name,
                "course_marks": course_marks,
                "exam_mark": exam_mark
            })
    return students

# Calculate total, percentage, grade
def calculate_student_info(student):
    coursework_total = sum(student["course_marks"])
    exam_mark = student["exam_mark"]
    overall_percentage = ((coursework_total + exam_mark) / 160) * 100
    if overall_percentage >= 70:
        grade = "A"
    elif overall_percentage >= 60:
        grade = "B"
    elif overall_percentage >= 50:
        grade = "C"
    elif overall_percentage >= 40:
        grade = "D"
    else:
        grade = "F"
    return coursework_total, overall_percentage, grade

# Display student info in text widget
def display_student(student, text_widget):
    coursework_total, overall_percentage, grade = calculate_student_info(student)
    text_widget.insert(tk.END, f"Name: {student['name']}\n")
    text_widget.insert(tk.END, f"Student Code: {student['code']}\n")
    text_widget.insert(tk.END, f"Total Coursework: {coursework_total}/60\n")
    text_widget.insert(tk.END, f"Exam Mark: {student['exam_mark']}/100\n")
    text_widget.insert(tk.END, f"Overall Percentage: {overall_percentage:.2f}%\n")
    text_widget.insert(tk.END, f"Grade: {grade}\n")
    text_widget.insert(tk.END, "-"*40 + "\n")

# GUI functions
def view_all_students():
    text_widget.delete("1.0", tk.END)
    for student in students:
        display_student(student, text_widget)
    avg_percentage = sum(calculate_student_info(s)[1] for s in students)/len(students)
    text_widget.insert(tk.END, f"Number of students: {len(students)}\n")
    text_widget.insert(tk.END, f"Class average percentage: {avg_percentage:.2f}%\n")
    text_widget.insert(tk.END, "="*40 + "\n")

def view_individual_student():
    code = code_entry.get().strip()
    if not code.isdigit():
        messagebox.showerror("Error", "Please enter a valid numeric student code.")
        return
    code = int(code)
    text_widget.delete("1.0", tk.END)
    for student in students:
        if student["code"] == code:
            display_student(student, text_widget)
            return
    messagebox.showinfo("Not Found", "Student not found.")

def show_highest_student():
    text_widget.delete("1.0", tk.END)
    highest = max(students, key=lambda s: calculate_student_info(s)[1])
    display_student(highest, text_widget)

def show_lowest_student():
    text_widget.delete("1.0", tk.END)
    lowest = min(students, key=lambda s: calculate_student_info(s)[1])
    display_student(lowest, text_widget)

# Main GUI
script_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_dir, "studentMarks.txt")
students = load_students(filename)

root = tk.Tk()
root.title("Student Manager")
root.geometry("700x600")

# Top frame for buttons and entry
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

view_all_btn = tk.Button(top_frame, text="View All Students", command=view_all_students)
view_all_btn.grid(row=0, column=0, padx=5)

highest_btn = tk.Button(top_frame, text="Highest Scorer", command=show_highest_student)
highest_btn.grid(row=0, column=1, padx=5)

lowest_btn = tk.Button(top_frame, text="Lowest Scorer", command=show_lowest_student)
lowest_btn.grid(row=0, column=2, padx=5)

code_label = tk.Label(top_frame, text="Enter Student Code:")
code_label.grid(row=1, column=0, pady=5)

code_entry = tk.Entry(top_frame)
code_entry.grid(row=1, column=1, pady=5)

view_individual_btn = tk.Button(top_frame, text="View Student", command=view_individual_student)
view_individual_btn.grid(row=1, column=2, pady=5, padx=5)

# Text widget for output
text_widget = tk.Text(root, width=80, height=30)
text_widget.pack(pady=10)

root.mainloop()
