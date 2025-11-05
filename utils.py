import os


def get_student_info():
    """Collects basic student information and number of subjects."""
    name = input("Enter Student Name: ").strip()
    roll = input("Enter Roll Number: ").strip()

    while True:
        try:
            num_subjects = int(input("Enter number of subjects: "))
            if num_subjects > 0:
                break
            else:
                print("Number of subjects must be greater than 0.")
        except ValueError:
            print("Please enter a valid integer for number of subjects.")

    return {"name": name, "roll": roll, "num_subjects": num_subjects}


def get_subjects_and_marks(num_subjects):
    """Collects subject names and validated marks."""
    subjects = []
    for i in range(num_subjects):
        subject = input(f"Enter name of subject {i+1}: ").strip()

        # Input validation for marks
        while True:
            try:
                mark = float(input(f"Enter marks for {subject}: "))
                if 0 <= mark <= 100:
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number for marks.")

        subjects.append({"name": subject, "mark": mark})

    return subjects


def calculate_total(marks):
    """Returns the total of all marks."""
    return sum(marks)


def calculate_average(total, num_subjects):
    """Returns the average marks."""
    if num_subjects == 0:
        return 0
    return total / num_subjects


def get_grade(average):
    """Determines grade based on average."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def format_report(student, total, average, grade):
    """Formats the report card into a neat string."""
    lines = []
    lines.append("\n===== REPORT CARD =====")
    lines.append(f"Name       : {student['name']}")
    lines.append(f"Roll Number: {student['roll']}")
    lines.append("----------------------------")

    for sub in student["subjects"]:
        lines.append(f"{sub['name']:<12}: {sub['mark']:.2f}")

    lines.append("----------------------------")
    lines.append(f"Total Marks : {total:.2f}")
    lines.append(f"Average     : {average:.2f}")
    lines.append(f"Grade       : {grade}")
    lines.append("============================\n")

    return "\n".join(lines)


def save_report(student, report):
    """Saves the report card as a text file."""
    # Create folder if it doesn't exist
    os.makedirs("data", exist_ok=True)
    safe_name = student['name'].strip().replace(" ", "_") or "student"
    safe_roll = student['roll'].strip() or "roll"
    filename = f"data/{safe_name}_{safe_roll}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)
