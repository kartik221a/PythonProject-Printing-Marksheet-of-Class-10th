from tabulate import tabulate

def calculate_grade(marks):
    if marks >= 80:
        return 'A+'
    elif 70 <= marks < 80:
        return 'A'
    elif 60 <= marks < 70:
        return 'B'
    elif 50 <= marks < 60:
        return 'C'
    elif 33 <= marks < 50:
        return 'D'
    else:
        return 'F'


"""Taking input from the user"""
while True:
    valid_name = True
    student_name = input("\nEnter student name : ").title()
    for i in student_name:
        if not (i.isalpha() or i.isspace()):
            valid_name = False
            print("\nEnter the valid name!!!")
            break
    if valid_name:
        break

while True:
    valid_name = True
    mother_name = input("\nEnter mother's name : ").title()
    for i in mother_name:
        if not (i.isalpha() or i.isspace()):
            valid_name = False
            print("\nEnter the valid name!!!")
            break
    if valid_name:
        break

while True:
    valid_name = True
    father_name = input("\nEnter father's name : ").title()
    for i in father_name:
        if not (i.isalpha() or i.isspace()):
            valid_name = False
            print("\nEnter the valid name!!!")
            break
    if valid_name:
        break

while True:
    try:
        roll_no = int(input("\nEnter roll number : "))
        if roll_no > 0:
            break
        else:
            print("\nEnter valid roll no.!!!")
    except ValueError:
        print("\nEnter valid roll no.!!!")

subjects = ["Hindi", "English", "Mathematics", "Science", "Social Science", "Commerce"]
subject_marks = []
subject_status = [""] * len(subjects)


for i in subjects:
    while True:
        try:
            sub = int(input(f"\nEnter {i} marks : "))
            if 0 <= sub <=100:
                break
            else:
                print("\nEnter valid marks!!!")
                
        except ValueError:
            print("\nEnter valid marks!!!")
    subject_marks.append(sub)

# Checking conditions for pass or fail in each subject
def apply_grace(subject_marks):
    if 31 <= subject_marks < 33:
        grace = max(33 - subject_marks, 0)
        return 33, f"Grace of {grace} marks added"
    elif subject_marks <31:
        return subject_marks, "Fail"
    else:
        return subject_marks, "Pass"


for i in range(len(subjects)):
    subject_marks[i], subject_status[i] = apply_grace(subject_marks[i])


# Calculating total marks, percentage, CGPA and result_status
total_marks = sum(subject_marks)
percentage = round((total_marks / (len(subjects)*100)) * 100, 2)
cgpa = round(percentage / 9.5, 2)


def result_status(subject_status):
    failed_subjects = []
    for i in range(len(subjects)):
        if subject_status[i] == "Fail":
            failed_subjects.append(1)
        else:
            failed_subjects.append(0)
    failed_subjects = sum(failed_subjects)
            
    grace_count = []
    for i in range(len(subjects)):
        if subject_status[i].endswith("added"):
            grace_count.append(1)
        else:
            grace_count.append(0)
    grace_count = sum(grace_count)
    
    if failed_subjects <= 1 and grace_count <= 2 and percentage >= 33.0:
        return "Pass"
    else:
        return "Fail"


"""Generating the marksheet template"""

"""Generating marksheet super prefix"""
marksheet_super_prefix = f"""

{"+"*125}

                    BOARD OF HIGHSCHOOL AND INTERMEDIATE EDUCATION, U.P.
                        HIGH SCHOOL EXAMINATION - 2019
                            CERTIFICATE-CUM-MARKS SHEET

"""


"""Generating marksheet sub info"""
marksheet_info = [
                ["Roll No.", "Distt./Centre/School code", "Regular/Private", "Exam Type", "Certificate No."],
                [roll_no, "12/11178/1002", "Regular", "Full Exam", 12311638]
                ]

marksheet_info = tabulate(marksheet_info, stralign="center")


"""Generating marksheet prefix"""
marksheet_prefix = f"""
This is to certify that, according to the board's record {student_name} son/daughter of 
Mrs. {mother_name} and Mr. {father_name} has passed High School Examination held in February 
(2019) from School/Centre S.D. Inter College, Sadar, Meerut.

"""


"""Generating Marksheet"""
def marksheet():
    data = []
    for i in range(len(subjects)):
        data.append([subjects[i], 100, subject_marks[i], calculate_grade(subject_marks[i]), subject_status[i]])

    table = tabulate(data, headers = ["Subject", "Max. Marks", "Obtained Marks", "Grade", "Result"], tablefmt="grid")
    print(table)


"""Generating Marksheet suffix"""
marksheet_suffix = f"""
Total Marks                                             :                 {total_marks}
Percentage                                              :                 {percentage}%
CGPA                                                    :                 {cgpa}
Category of Moral, Yoga, Sports and Physical Education  :                 A
Pass/Fail Status                                        :                 {result_status(subject_status)}

Candidate clearing any 05 subjects out of 06 will be declared pass.       No divisions are awarded
candidate who have grace only in 2 subjects will be pass.
  *Grace will provide only when candidates marks are above than 30.


For result verification visit website : www.upsp.edu.in or upmspresults.up.nic.in

Date    :   27th April 2019
Place   :   Prayagraj, Uttar Pradesh                                       Neena Srivastava
Note    :   For important Instructions see overleaf.                          (secretary)

{"+"*125}
"""


"""Printing marksheet"""
print(marksheet_super_prefix)
print(marksheet_info)
print(marksheet_prefix)
marksheet()
print(marksheet_suffix)