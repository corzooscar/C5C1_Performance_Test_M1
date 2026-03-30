# ──── Save inventory to CSV file ─────────────────────────────────────────────────────────────────────────────────────
def save_csv(Students, path, include_header=True):
    """
    Writes the current Students list to a CSV file at the given path.

    Each student is saved as a comma-separated row with the respective 
    fields. If include_header is True, a header row is written first.
    Returns early with a warning if the Student list is empty. Catches any
    file system errors (permissions, invalid path, etc.) without closing the program.

    Args:
        Students(list): The current list of students dictionaries.
                          Each product must have keys: "id" (int), "name" (str), "age" (int), "program" (str), "status" (str).
        path (str): The file path where the CSV will be saved (e.g. "inventory.csv").
        include_header (bool): Whether to write the header row "name,price,quantity". Defaults to True.

    Returns:
        None. Prints a success or error message to the terminal.
    """
    if not Students:
        print(f"Students list is empty.".center(60))
        return

    try:
        with open(path, "w") as file:
            if include_header:
                file.write("id,name,age,program,status\n")

            for s in Students:                                                                  #Here "s" stands for the word student, but that doesn't change anything,  
                file.write(f"{s['id']},{s['name']},{s['age']},{s['program']},{s['status']}\n")  #i could use any other symbol as long as i keep it in the structure afterwards     
                                                                                                #in the previous line we can see it        
        print(f"Inventory saved in: {path}")                                                    

    except Exception as e:
        print(f"Error saving file: {e}")


# ──── Load Students from CSV file ─────────────────────────────────────────────────────────────────────────────────────
def load_csv(path):
    """
    Reads a CSV file and returns its contents as a list of students dictionaries.

    Validates the header row, then processes each data row individually.
    Rows with the wrong number of columns, non-numeric price/quantity, or
    negative values are skipped and counted as invalid. Handles missing files,
    encoding errors, and any other exceptions without closing the program.

    Args:
        path (str): The file path of the CSV to load (e.g. "STUDENTS.csv").

    Returns:
        tuple:
            - list: Students successfully parsed from the file. Empty list if the file
                    could not be read or had no valid rows.
            - int:  Number of rows skipped due to validation errors.
    """
    Students = []
    invalid_rows = 0

    try:
        with open(path, "r") as file:
            lines = file.readlines()

        # Validate header
        if lines[0].strip() != "id,name,age,program,status":
            print(f"Invalid file format.")
            return [], 0

        for line in lines[1:]:
            parts = line.strip().split(",")

            if len(parts) != 3:
                invalid_rows += 1
                continue

            id, name, age, program, status = parts

            try:
                price = float(price)
                quantity = int(quantity)

                if price < 0 or quantity < 0:
                    invalid_rows += 1
                    continue

                Students.append({
                    "id": id,
                    "name": name,
                    "age": age,
                    "program": program,
                    "status": status
                })

            except ValueError:
                invalid_rows += 1

        return Students, invalid_rows

    except FileNotFoundError:
        print(f"File not found.")
        return [], 0
    except UnicodeDecodeError:
        print(f"File encoding error.")
        return [], 0
    except Exception as e:
        print(f"Error loading file: {e}")
        return [], 0