# Full name: Cristopherson T. Domantay
# Section: IV-BSIT-C

PASSING_GRADE = 75


def read_grades():
    while True:
        try:
            count = int(input("Number of grades: "))
            if count > 0:
                break
        except ValueError:
            pass
        print("Enter a positive whole number.")

    grades = []
    while len(grades) < count:
        try:
            grade = float(input(f"Grade {len(grades) + 1}: "))
            if 0 <= grade <= 100:
                grades.append(grade)
                continue
        except ValueError:
            pass
        print("Enter a number from 0 to 100.")
    return grades


def average(grades):
    return sum(grades) / len(grades)


def highest(grades):
    return max(grades)


def lowest(grades):
    return min(grades)


def pass_status(grades):
    return "Pass" if average(grades) >= PASSING_GRADE else "Fail"


def main():
    grades = []
    while True:
        print("\n1. Enter grades\n2. View results\n3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            grades = read_grades()
        elif choice == "2":
            if not grades:
                print("Enter grades first.")
                continue
            print(f"Average: {average(grades):.2f}")
            print(f"Highest: {highest(grades):g}")
            print(f"Lowest: {lowest(grades):g}")
            print(f"Status: {pass_status(grades)}")
        elif choice == "3":
            return
        else:
            print("Choose 1, 2, or 3.")


if __name__ == "__main__":
    main()

# The variable count is local to read_grades and is only available inside that function.
# PASSING_GRADE is defined at module level, so pass_status can read it directly.
# The grades parameter is local to each calculation and receives the list from its caller.
