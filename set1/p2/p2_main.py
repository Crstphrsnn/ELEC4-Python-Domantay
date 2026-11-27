# Full name: Cristopherson T. Domantay
# Section: IV-BSIT-C

from datetime import datetime

import student_utils


def read_grades():
    while True:
        entries = input("Enter grades separated by commas: ").split(",")
        try:
            grades = [float(entry.strip()) for entry in entries]
            if all(0 <= grade <= 100 for grade in grades):
                return grades
        except ValueError:
            pass
        print("Enter one or more numbers from 0 to 100, such as 60,80.")


def main():
    grades = read_grades()
    print(f"Report generated: {datetime.now():%Y-%m-%d %H:%M:%S}")
    print(f"Average: {student_utils.average(grades):.2f}")
    print(f"Highest: {student_utils.highest(grades):g}")
    print(f"Lowest: {student_utils.lowest(grades):g}")
    print(f"Status: {student_utils.pass_status(grades)}")


if __name__ == "__main__":
    main()
