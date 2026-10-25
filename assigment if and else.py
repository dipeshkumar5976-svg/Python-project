# project 1
# correct_pin = "1234"
# balance = 10000
# attempts = 3
# while attempts > 0:
#     entered_pin = input("Enter PIN: ")
#     if entered_pin == correct_pin:
#         break
#     attempts -= 1
#     if attempts > 0:
#         print(f"Wrong PIN. Attempts left: {attempts}")
#     else:
#         print("Card blocked.")


# if attempts > 0:
#     while True:
#         print("\n1. Balance\n2. Deposit\n3. Withdraw\n4. Exit")
#         choice = input("Choose an option: ")

#         if choice == "1":
#             print(f"Balance: {balance}")
        
#         elif choice == "2":
#             amount = float(input("Enter deposit amount: "))
#             if amount > 0:
#                 balance += amount
#                 print(f"New balance: {balance:.0f}")
#                 history.append(f"Deposit {amount:.0f}")
#             else:
#                 print("Amount must be above 0.")
        
#         elif choice == "3":
#             amount = float(input("Enter withdraw amount: "))
#             if amount <= balance:
#                 balance -= amount
#                 print(f"New balance: {balance:.0f}")
#             else:
#                 print("Insufficient balance")
        
#         elif choice == "4":
#             print("Thank you!")
#             break
#         else:
#             print("Invalid option. Please try again.")


#project=2
# Starter data

students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}
while True:
    print("\n1. Add student\n2. View all\n3. Show topper\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        if name in students:
            print("Student already exists.")
            continue
        marks = []
        marks_collected = 0
        while marks_collected < 3:
                mark = int(input(f"Enter mark {marks_collected + 1} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    marks_collected += 1
                else:
                    print("Invalid mark, try again.")
        
students[name] = marks

    elif choice == "2":
    
        for student, marks in students.items():
            average = sum(marks) / len(marks)
            
            if average >= 85:
                grade = "A"
            elif average >= 70:
                grade = "B"
            elif average >= 50:
                grade = "C"
            else:
                grade = "F"
                
            print(f"{student} {average:.2f} {grade}")

    elif choice == "3":
        topper_name = None
        highest_average = -1
        
        for student, marks in students.items():
            average = sum(marks) / len(marks)
            if average > highest_average:
                highest_average = average
                topper_name = student
                
        print(f"Topper: {topper_name}")

    elif choice == "4":
        print("Goodbye!")
        break







         
   
   