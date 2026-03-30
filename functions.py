
# ──── Reusable input function ────────────────────────────────────────────────────────────────────────────────────
def get_info(prompt, type=str):
    """
    Repeatedly prompts the user until a valid value of the given type is entered.

    Catches ValueError for non-convertible input. For numeric types (int, float),
    also rejects values lower than 1.

    Args:
        prompt (str): The message shown to the user in the terminal.
        type (type): The expected data type for the input. Defaults to str.

    Returns:
        The user's input converted to the specified type.
    """
    keep_going = "y"
    while keep_going != "n":                # Infinite loop to keep asking until valid input is received        
        try:
            value = type(input(prompt))
            if type == int or type == float:
                if value < 1:
                    print(f"❌ Value cannot be lower than 1. Try again. ❌\n")
                    continue
            keep_going = "n"
        except ValueError:
            print(f"❌ Invalid input. Try again. ❌\n")
    return value
# ─────────────────────────────────────────────────────────────────────────────
# STUDENT REGISTRATION
# ─────────────────────────────────────────────────────────────────────────────
# ──── 0. Find Student ──────────────────────────────────────────────────────────────────────────────────── 
def find_student(Students, student_id):
    """
    Search for a student by ID in the  Students list.

    Parameters:
         Students (list): list of Student dicts
         student_id (int): the ID to search for
    Returns:
        dict | None: the student dict if found, None otherwise.
    """
    # Use next() with a generator — returns the first match or None
    return next((s for s in Students if s["id"] == student_id), None)

# ──── 1. Add Student ──────────────────────────────────────────────────────────────────────────────────── 
def register_students(Students):
    """
    Prompt the user for client data and add them to the  Students list.

    Validates that the ID is not empty and not already registered.

    Parameters:
         Students (list): the current list of  Students (modified in place)
    Returns:
        list: the updated  Students list.
    """
    student_id = get_info(f"~ Student ID: ", int)

    if find_student( Students,  student_id):
        print(f"❌ ERROR: Client '{ student_id}' is already registered. ❌\n".center(60))
        return  Students

    name = get_info(f"~ Student Name: ").strip()
 
    
    age = get_info(f"~ Student Age: ", int)

    
    program = get_info(f"~ Student Program: ", str).strip()
 
    
    will_of_god = True
    while will_of_god:
        status = input("~ Please determine Student's current status\n  ('A':Active or 'I':Inactive): ").upper().strip()
        if status not in ["A", "I"]:
            print("❌ ERROR: Status should be either 'A'(ACTIVE) or 'I'(INACTIVE),\n  please try again ❌\n")
            continue
        else:
            will_of_god = False

    Students.append({"id":  student_id, "name": name, "age": age, "program": program, "status": status})
    print(f"Student '{name}' registered successfully.\n".center(60))
    return  Students

# ─────────────────────────────────────────────────────────────────────────────
# CHECK STUDENTS
# ─────────────────────────────────────────────────────────────────────────────
# ──── 1. Show Student List ──────────────────────────────────────────────────────────────────────────────────── 
def show_students(Students):
    """
    Prints all students in the Students list to the terminal.

    If the Students list is empty, displays a warning message and returns early.
    Otherwise, iterates over the list and prints each value for every key with 
    a separator line between entries.

    Args:
        Students (list): The current list of product dictionaries.

    Returns:
        None.
    """
    if not Students:
        print(f"The Students list is currently empty.\n")
        return
    else:
        for student in Students:
            print(f"""— ID: {student['id']}
— Name: {student['name']} 
— Age: {student['age']} 
— Program: {student['program']}
— Status: {student['status']}""")
            print(f"{'─'*50}")
            
# ─────────────────────────────────────────────────────────────────────────────
# SEARCH STUDENTS
# ─────────────────────────────────────────────────────────────────────────────
# ──── 1. Search Specific Student by id ──────────────────────────────────────────────────────────────────────────────────── 
def find_spstudent(Inventory, id):
    """
    Searches the inventory for a product matching the given name.

    Performs a case-sensitive linear search through the inventory list.
    Used internally by update_product() and delete_product().

    Args:
        Students (list): The current list of students dictionaries.
        id (int): The exact product name to search for.

    Returns:
        dict: The matching product dictionary if found.
        None: If no product with that name exists.
    """
    for product in Inventory:
        if product['id'] == id:
            return product
    return None

# ─────────────────────────────────────────────────────────────────────────────
# UPDATE STUDENTS INFORMATION
# ─────────────────────────────────────────────────────────────────────────────
# ──── 1. Update Student Info ──────────────────────────────────────────────────────────────────────────────────── 
def update_studentinfo(Students, id, new_name=None, new_age=None, new_program=None, new_status=None):
    """
    Updates the price and/or quantity of an existing product.

    Uses find_product() to locate the product by name. Only updates
    the fields that are explicitly passed (not None). If the product
    is not found, returns False without modifying the inventory.

    Args:
        Inventory (list): The current list of product dictionaries.
        name (str): The exact name of the product to update.
        new_price (float, optional): New price to set. Defaults to None (no change).
        new_quantity (int, optional): New quantity to set. Defaults to None (no change).

    Returns:
        bool: True if the product was found and updated, False otherwise.
    """
    student = find_spstudent(Students, id)

    if student:
        if new_name is not None:
            student["name"] = new_name
        if new_age is not None:
            student["age"] = new_age
        if new_program is not None:
            student["program"] = new_program
        if new_status is not None:
            student["status"] = new_status
        return True

    return False

# ─────────────────────────────────────────────────────────────────────────────
# DELETE A STUDENT FROM THE LIST
# ─────────────────────────────────────────────────────────────────────────────
# ──── 1. Delete Student ──────────────────────────────────────────────────────────────────────────────────── 
def delete_student(Students, id):
    """
    Removes a student from the list by id.

    Uses find_spstudent() to locate the product, then removes it from the list
    using list.remove(). If the product does not exist, returns False.

    Args:
        Students (list): The current list of student dictionaries.
        id (int): The exact id of the student to delete.

    Returns:
        bool: True if the student was found and removed, False otherwise.
    """
    student = find_spstudent(Students, id)

    if student:
        Students.remove(student)
        return True 

    return False
