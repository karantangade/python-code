
employees = [
    (201, 'Rahul', 45000),
    (202, 'Priya', 52000)
]

while True:
    print("\n===== Employee Data Management System =====")
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        empid = int(input("Enter Employee ID: "))
        ename = input("Enter Employee Name: ")
        esal = float(input("Enter Employee Salary: "))

        employees.append((empid, ename, esal))
        print("Employee added successfully!")

    elif choice == 2:
        print("\nEmployee Details:")

        for emp in employees:
            print("Employee ID:", emp[0],
                  "| Name:", emp[1],
                  "| Salary:", emp[2])

    elif choice == 3:
        search_id = int(input("Enter Employee ID to search: "))
        found = False

        for emp in employees:
            if emp[0] == search_id:
                print("Employee Found!")
                print("Employee ID:", emp[0])
                print("Employee Name:", emp[1])
                print("Employee Salary:", emp[2])
                found = True
                break

        if not found:
            print("Employee not found!")

    elif choice == 4:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1 to 4.")
