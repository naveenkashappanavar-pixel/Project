def average(marks):
    return sum(marks) / len(marks)


def grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg < 90:
        return "A"
    elif 65 <= avg < 80:
        return "B"
    elif 50 <= avg < 65:
        return "C"
    elif 40 <= avg < 50:
        return "D"
    else:
        return "F"


def is_pass(marks):
    return all(mark >= 40 for mark in marks)


def main():
    print("STUDENT GRADE CALCULATOR")

    name = input("Enter student name: ")

    marks = []
    for i in range(1, 4):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    avg = average(marks)
    result_grade = grade(avg)
    result = is_pass(marks)

    print("\n----- STUDENT RESULT -----")
    print("Name:", name)
    print("Marks:", marks)
    print("Average:", round(avg, 2))
    print("Grade:", result_grade)
    print("Pass:", result)


if __name__ == "__main__":
    main()