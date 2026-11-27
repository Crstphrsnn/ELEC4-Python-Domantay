# Full name: [Your full name] | Section: [Your section] | Activity: P2 | Date: 2026-11-23

PASSING_GRADE = 75


def average(grades):
    return sum(grades) / len(grades)


def pass_status(grades):
    return "Pass" if average(grades) >= PASSING_GRADE else "Fail"


def highest(grades):
    return max(grades)


def lowest(grades):
    return min(grades)
