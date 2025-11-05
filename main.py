from utils import (
    get_student_info,
    get_subjects_and_marks,
    calculate_total,
    calculate_average,
    get_grade,
    format_report,
    save_report
)


def main():
    print("=== STUDENT REPORT CARD GENERATOR ===\n")

    # Step 1: Get basic info (includes number of subjects)
    student = get_student_info()            # returns dict with 'name','roll','num_subjects'

    # Defensive check: ensure num_subjects exists and is an int > 0
    if "num_subjects" not in student or not isinstance(student["num_subjects"], int) or student["num_subjects"] <= 0:
        print("Internal error: number of subjects missing or invalid.")
        return

    # Step 2: Get subjects & marks (pass the number)
    student["subjects"] = get_subjects_and_marks(student["num_subjects"])

    # Step 3: Calculations
    marks = [sub["mark"] for sub in student["subjects"]]
    total = calculate_total(marks)
    average = calculate_average(total, len(marks))
    grade = get_grade(average)

    # Step 4: Display report
    report = format_report(student, total, average, grade)
    print(report)

    # Step 5: Optionally save
    save_choice = input("Do you want to save this report? (y/n): ").strip().lower()
    if save_choice == "y":
        save_report(student, report)
        print("Report saved successfully!")
    else:
        print("Report not saved.")

    print("\nThank you for using the Report Card Generator!")


if __name__ == "__main__":
    main()
