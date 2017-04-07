student_list=[]

def create_student():
    # ask for student's name
    name = input("Enter new student's name: ")
    # create dictionary
    student_data = {
        "name": name,
        "marks" :[]
    }
    # return dictionary
    return student_data

def add_mark(student, mark):
    # append marks to the dictionary
    student["marks"].append(mark)

def calculate_average_marks(student):
    number = len(student["marks"])
    if number==0:
        return 0

    total_sum = sum(student["marks"])
    return total_sum/number

def student_details(student):
    print("{},average marks: {}.".format(student["name"],
                                        calculate_average_marks(student)))


def print_student_list(students):
    for i,student in enumerate(students):
        print("ID: {}.".format(i))
        student_details(student)

def menu():
    selection = input("Enter 'p' to print the student list, "
                      "'s' to add a new student, "
                      "'a' to add a mark to a student, "
                      "or 'q' to quit. "
                      "Enter your selection: ")

    while selection!='q':
        if selection== "p" :
            print_student_list(student_list)
        elif selection== "s":
            student_list.append(create_student())
        elif selection== "a":
            student_id = int(input("enter  student ID to add marks to: "))
            student = student_list[student_id]
            new_marks = int(input("Enter new marks: "))
            add_mark(student,new_marks)

        selection = input("Enter 'p' to print the student list, "
                      "'s' to add a new student, "
                      "'a' to add a mark to a student, "
                      "or 'q' to quit. "
                      "Enter your selection: ")

menu()