students={}
# stud = input("Enter student name: ")
# marks = int(input("Enter student marks: "))
# students[stud] = marks
# def numOfStudent():
#     num = print(int(input("Number of students you want to insert: ")))
def addStudent():
    # for i in range(numOfStudent):
    while True:
        stud = input("Enter student name or leave it blank to exit entry: ")
        if stud == "":
            break
        try:
            marks = int(input("Enter student marks(between 0 to 100): "))
            if marks < 0 or marks > 100:
                print("Invalid input. Please enter a valid number for marks between 0 and 100.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number for marks.")
            continue
        if stud in students:
            students[stud].append(marks)
        else:
            students[stud] = [marks]
def showStudent():
    if not students:
        print("No student found")
        return
    for name,marks in students.items():
        print(name,"->",marks)
def searchStudent(name):
    # name = input("Enter student name to search: ") line no 63 you are asking twice to enter the student name
    if name in students:
        print(name,"->",students[name])
    else:
        print("Student not found")
def updateStudent():
    std = input("Enter student name to update: ")
    # while True: always this will false why ? buz of i am taking in input as int() but i am checking it with string in if condition
    #     mark = int(input("Enter new marks: "))
    #     if mark == "": False always
    #         break
    try:
        mark = int(input("Enter new marks(between 0 to 100): "))
        if mark < 0 or mark > 100:
            print("Invalid input. Please enter a valid number for marks between 0 and 100.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number for marks.")
        return
    if std in students:
        students[std] = [mark]
        print("Student mark updated successfully")
    else:
        print("Student not found")
def delStudent():
    studs = input("Enter student name to delete: ")
    if studs in students:
        del students[studs]
        print("Student deleted successfully")
    else:
        print("Student not found")
def main():
    while True:
        # print("0. Number of Students")
        print("1. Add Student")
        print("2. Show Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        # if choice == 0:
        #     numOfStudent()
        if choice == 1:
            addStudent()
        elif choice == 2:
            showStudent()
        elif choice == 3:
            name = input("Enter student name to search: ")
            # try: dont need to use this try and except block cz i am checking this condition in searchStudent function
            #     searchStudent(name)
            # except NameError:
            #     print("Invalid input. Please enter a valid name.")
            #     continue
            searchStudent(name)
        elif choice == 4:
            updateStudent()
        elif choice == 5:
            delStudent()
        elif choice == 6:
            break
        else:
            print("Invalid choice")
if __name__ == '__main__':
    main()