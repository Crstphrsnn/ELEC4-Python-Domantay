# Full name: [Your full name] | Section: [Your section] | Activity: P4 | Date: 2026-11-23


def divide_numbers():
    try:
        numerator = float(input("First number: "))
        denominator = float(input("Second number: "))
        result = numerator / denominator
    except ValueError:
        print("Invalid number. Enter numeric input.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"Result: {result:g}")
    finally:
        print("Division attempt finished.")


def display_file():
    filename = input("Text file name: ").strip()
    try:
        with open(filename, encoding="utf-8") as source:
            print(source.read())
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except (OSError, UnicodeDecodeError, ValueError):
        print(f"Unable to read as text: {filename}")


def main():
    while True:
        print("\n1. Divide\n2. Open file\n3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            divide_numbers()
        elif choice == "2":
            display_file()
        elif choice == "3":
            return
        else:
            print("Invalid menu choice. Select 1, 2, or 3.")


if __name__ == "__main__":
    main()
