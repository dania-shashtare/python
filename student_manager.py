import re
import datetime
# enter name
while True:
    try:
        name = input("Enter student name: ")
        if not re.fullmatch(r'[a-zA-Z\s]+', name):
            raise ValueError("Invalid name format")
        break
    except ValueError as e:
        print(e)
        name = input("Invalid name format try again:")
# enter age
while True:
    try:
        age = input("Enter student age: ")
        if not re.fullmatch(r'[0-9]+', age):
            raise ValueError("Invalid age format")
        age = int(age)
        if age <= 0:
            raise ValueError("Invalid age")
        break
    except ValueError as e:
        print(e)
        age = input("Invalid age try again:")
# enter email
while True:
    try:
        email = input("Enter student email: ")
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format")
        break
    except ValueError as e:
        print(e)
        email = input("Invalid email format try again:")
# enter marks
while True:
    try:
        marks = input("Enter student marks separated by comma: ")
        marks = [int(x) for x in marks.split(',')]
        if not marks:
            raise ValueError("Invalid marks format")
        break
    except ValueError as e:
        print(e)
        marks = input("Invalid marks format try again:")

# enter major
while True:
    try:
        major = input("Enter student major: ")
        if not re.fullmatch(r'[a-zA-Z\s]+', major):
            raise ValueError("Invalid major format")
        break
    except ValueError as e:
        print(e)
        major = input("Invalid major format try again:")


def calculatemax(marks):
    return max(marks)


def calculatemin(marks):
    return min(marks)


def calculateaverage(marks):
    return sum(marks) / len(marks)


def calculategrade(marks):
    average = calculateaverage(marks)
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "E"


def emailstatus(email):
    pattern = r"[^@]+@[^@]+\.[^@]+"
    if re.fullmatch(pattern, email):
        return "Valid"
    else:
        return "Invalid"


def majormsg(major):
    if major.lower() == "computer science" or major.lower() == "computer engineering":
        return "You are in the technology field."
    else:
        return "You might want to consider switching to Computer Engineering."


def reportDate():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def jsonreport():
    report = {
        "name": name,
        "age": age,
        "email": email,
        "major": major,
        "marks": marks,
        "max": calculatemax(marks),
        "min": calculatemin(marks),
        "average": calculateaverage(marks),
        "grade": calculategrade(marks),
        "email_status": emailstatus(email),
        "major_status": majormsg(major),
        "report_date": reportDate()
    }
    return report


print("===== Student Report =====")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Email: {email}")
print(f"Major: {major}")
print("\n")
print("===== Student Marks =====")
print(marks)
print(f"Max: {calculatemax(marks)}")
print(f"Min: {calculatemin(marks)}")
print(f"Average: {calculateaverage(marks):.2f}")
print(f"Grade: {calculategrade(marks)}")
print(f"Email Status: {emailstatus(email)}")
print(f"Major Status: {majormsg(major)}")
print(f"Report Date: {reportDate()}")
print("\n")
print("===== JSON Report =====")
print(jsonreport())
