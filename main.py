from functions import *
from database import *

DATABASE = "database.csv"

Students = []
Showtime = True


# Welcome banner
print(f"""╔═══════════════════════════════════════════════════════════╗
            🐧📦  STUDENTS MANAGER SYSTEM  📦🐧
              Welcome to the Students Manager!
    By: Oscar Corzo | GitHub: https://github.com/corzooscar 
╚═══════════════════════════════════════════════════════════╝""")

# ── MENU ─────────────────────────────────────────────────────────────────────

# Main loop
while Showtime:
    try:
        Option = int(input(f"""{"="*24} MAIN MENU {"="*25}
1) Register a new Student
2) Check Students List
3) Check specific Student
4) Update Student Information
5) Delete Student Information
6) 🔚​ Exit
{"="*60}
Choose an option:
➤  """))

        # Option 1 — Enters a sub-loop that keeps adding products until the user types 'exit'
        if Option == 1:
            Process = None
            while Process != "exit":
                print(f"{'='*23} NEW STUDENT {'='*24}")
                register_students(Students)
                
                
                
                Process = input(f"Type 'exit' to return to the main menu, or press Enter to\nregister another student: \n➤ ").lower().strip()
                
        # Option 2 — Displays all students currently registered in the list
        elif Option == 2:
            print(f"{'='*25} STUDENTS {'='*25}")            
            show_students(Students)

        # Option 3 — Search for a student
        elif Option == 3:
            print(f"{'='*22} SEARCH STUDENT {'='*22}")            
            id = int(input(f"~ Enter Student's ID: "))
            product = find_spstudent(Students, id)
            print(f"{product if product else 'Not found'}")

        # Option 4 — Update student info
        elif Option == 4:
            print(f"{'='*19} UPDATE STUDENT INFO {'='*20}")
            id = get_info(f"~ Student ID: ", int)
            name = get_info(f"~ Student's New Name: ").strip()   
            age = get_info(f"~ Student's New Age: ", int)
            program = get_info(f"~ Student's New Program: ", str).strip()
            will_of_god = True
            while will_of_god:
                status = input("~ Please determine Student's current status\n  ('A':Active or 'I':Inactive): ").upper().strip()
                if status not in ["A", "I"]:
                    print("❌ ERROR: Status should be either 'A'(ACTIVE) or 'I'(INACTIVE)\n  please try again ❌")
                    continue
                else:
                    will_of_god = False
                    updated = update_studentinfo(Students, id, name, age, program, status)
            print(f"{'Updated' if updated else 'Not found'}")
            

        # Option 5 — Delete a Student
        elif Option == 5:
            print(f"{'='*22} DELETE STUDENT {'='*22}")
            id = get_info(f"~ Student ID: ", int)
            deleted = delete_student(Students, id)
            print(f"{'Deleted' if deleted else 'Not found'}")

        # Option 6 — Exits the program cleanly
        elif Option == 6:
            print(f"{'Exiting the program. Goodbye!'.center(60)}")
            exit()

        # Any other number — informs the user the option is out of range
        else:
            print(f"{'❌ ERROR: Please enter a number between 1 and 6. ❌'.center(60)}")
            
    # Non-integer input at the main menu — caught here so the program never crashes        
    except ValueError:
        print(f"{'❌ ERROR: Please enter a valid input. ❌'.center(60)}")
