# Full name: Cristopherson T. Domantay
# Section: IV-BSIT-C


def add_student(students, known_names):
    name = input("Name to add: ").strip()
    key = name.casefold()
    if not name:
        print("Enter a name.")
    elif key in known_names:
        print(f"{name} already exists.")
    else:
        students.append(name)
        known_names.add(key)
        print(f"Added {name}.")


def remove_student(students, known_names):
    key = input("Full name to remove: ").strip().casefold()
    if key not in known_names:
        print("Student not found.")
        return
    name = next(name for name in students if name.casefold() == key)
    students.remove(name)
    known_names.remove(key)
    print(f"Removed {name}.")


def search_students(students):
    query = input("Full or partial name: ").strip().casefold()
    if not query:
        print("Enter a search term.")
        return
    matches = [name for name in students if query in name.casefold()]
    print("Matches: " + ", ".join(matches) if matches else "No matches.")


def display_students(students):
    for number, name in enumerate(sorted(students, key=str.casefold), start=1):
        print(f"{number}. {name}")
    print(f"Total students: {len(students)}")


def main():
    students = []
    known_names = set()
    while True:
        print("\n1. Add\n2. Remove\n3. Search\n4. Display all\n5. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_student(students, known_names)
        elif choice == "2":
            remove_student(students, known_names)
        elif choice == "3":
            search_students(students)
        elif choice == "4":
            display_students(students)
        elif choice == "5":
            return
        else:
            print("Choose a number from 1 to 5.")


if __name__ == "__main__":
    main()

# A list holds the display names and lets the program iterate over them for search and display.
# A set holds unique comparison keys and supports quick membership checks.
# The program updates both collections when a student is added or removed.
