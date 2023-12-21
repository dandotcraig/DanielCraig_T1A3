import csv
import datetime
from rich import print


copied_file = []

def view_previous_workout(file_name):
    copied_file = []
    with open(file_name, 'r') as f:
        reader = csv.reader(f)

        headers = next(reader)
        print(f"Header: {headers}")

        for row in reader:
            copied_file.append(row)
    index = 1
    for row in range (len(copied_file)):
        print(f"Exercise {index}: {str(copied_file[row])}")
        index += 1
    
    return ""
        
def add_exercise(file_name):
    print("[green]You choose add a new exercise")
    while True:
        try:
            exercise_name = input("Enter your new exercise: ")
            if any(i.isdigit() for i in exercise_name):
                print("[red] :cross_mark: Exercise must not contain numbers, try again but with words this time. :cross_mark:")
                raise ValueError
        except ValueError as e:
            print(e)
        else:
            break

    while True:
        try:
            kilo = "kg"
            weight_number = str(input("Enter your weight in kgs: "))
            if kilo not in weight_number:
                print("[red] :cross_mark: Weight must contain a number in kgs :cross_mark: ")
                raise ValueError
        except Exception:
            print("[red] :cross_mark: Try again :cross_mark: ")
        else:
            break

    while True:
        try:
            set_number = int(input("Enter your sets: "))
        except ValueError:
            print("[red] :cross_mark: Sorry, needs to be be a number. :cross_mark: ")
            continue
        except Exception:
            print("[red] :cross_mark: Try again :cross_mark: ")
        else:
            break
    
    while True:
        try:
            rep_number = int(input("Enter your reps: "))
        except ValueError:
            print(" :cross_mark: Sorry, needs to be be a number. :cross_mark: ")
            continue
        except Exception:
            print("[red] :cross_mark: Try again :cross_mark: ")
        else:
            break

    
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([exercise_name, weight_number, set_number, rep_number])
    
    copied_file = []
    
    new_exercise = [exercise_name, weight_number, set_number, rep_number]

    with open(file_name, 'r') as f:
        reader = csv.reader(f)   
        for row in reader:
            copied_file.append(row)
    print("\nHere is your updated routine:\n")
    for i in range (len(copied_file)):
        print("Exercise " + str(int(i)) + ": " + (str(copied_file[i]))) 
    
    print(f"\nThis line {new_exercise} has been added")
    print("")




def update_exercise(file_name):
    print("[green]You choose update an exercise")
    # user input
    
    while True:
        exercise_name_update = input("Enter the correct name of the exercise you want to update: ")
        # list variable
        exercise_list = []
        # open file to read contents
        replaced_row = None
        with open(file_name, "r") as f:
            # new copy of the file
            reader = csv.reader(f)
            # loop through each row
            for row in reader:
                if (exercise_name_update != row[0]):
                    # we want it in the update cvs
                    exercise_list.append(row)
                else:
                    replaced_row = row
        if (replaced_row is None):
            print("[red] :cross_mark: Input does not match, try again. :cross_mark: ")
            continue
            
        else:
            break
                                
    print(replaced_row)

    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(exercise_list)

    copied_file = []

    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            copied_file.append(row)

    print("\nUpdate the exercises details: ")
    while True:
        try:
            exercise_name = input("Re-type or update " + replaced_row[0] + ": ")
            if any(i.isdigit() for i in exercise_name):
                print(" :cross_mark: Exercise must not contain numbers, try again but with words this time. :cross_mark: ")
                raise ValueError
        except ValueError as e:
            print(e)
        else:
            break

    while True:
        try:
            kilo = "kg"
            weight_number = str(input("Re-type or update, must be in kg " + replaced_row[1] + ": "))
            if kilo not in weight_number:
                print("[red] :cross_mark: Weight must contain a number in kgs :cross_mark: ")
                raise ValueError
        except Exception:
            print("[red] :cross_mark: Try again :cross_mark: ")
        else:
            break
    
    while True:
        try:
            set_number = int(input("Re-type or update " + replaced_row[2] + ": "))
        except ValueError:
            print("[red] :cross_mark: Sorry, needs to be be a number :cross_mark: ")
            continue
        except Exception:
            print("[red] :cross_mark: Try again :cross_mark: ")
        else:
            break
    
    while True:
        try:
            rep_number = int(input("Re-type or update " + replaced_row[3] + ": "))
        except ValueError:
            print("[red] :cross_mark: Sorry, needs to be be a number :cross_mark: ")
            continue
        except Exception:
            print("[red] :cross_mark: Try again :cross_mark: ")
        else:
            break
    
    
    
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([exercise_name, weight_number, set_number, rep_number])
    
    copied_file = []
    
    new_exercise = [exercise_name, weight_number, set_number, rep_number]

    with open(file_name, 'r') as f:
        reader = csv.reader(f)   
        for row in reader:
            copied_file.append(row)
    print("\nHere is your updated workout")
    for i in range (len(copied_file)):
        print("Exercise " + str(int(i)) + ": " + (str(copied_file[i]))) 
    print(f"\nThis line has been updated to {new_exercise}")
    print("")
    




def remove_exercise(file_name):

    while True:
        print("[green]You selected to delete an exercise")
        # user input
        exercise_name_remove = input("Enter the name of the exercise you want to remove: ")
        # list variable
        exercise_list = []
        # open file to read contents
        replaced_row = None
        with open(file_name, "r") as f:
            # new copy of the file
            reader = csv.reader(f)
            # loop through each row
            for row in reader:
                # if its not the input
                if (exercise_name_remove != row[0]):
                    # we want it in the update cvs
                    exercise_list.append(row)
                else:
                    replaced_row = row

        if (replaced_row is None):
            print("[red] :cross_mark: Input does not match, try again.  :cross_mark: ")
            continue
        else:
            break

    # now we copy it over without the user input
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(exercise_list)
    
    copied_file = []
    
    with open(file_name, 'r') as f:
        reader = csv.reader(f)   
        for row in reader:
            copied_file.append(row)
    print("\nHere is your updated workout")
    for i in range (len(copied_file)):
        print("Exercise " + str(int(i)) + ": " + (str(copied_file[i])))
    
    print(f"\nThis line {replaced_row} has been removed")
    print("")
    return ""


def view_history(history):
    print("Here are all your previous workouts: ")
    
    pull_history = []
    
    with open(history, 'r') as f:
        puller = csv.reader(f)   
        for row in puller:
            pull_history.append(row)
    
    print(pull_history)
    return ""

def save_exit(file_name, history):
    print("[blue]You selected exit and log your workout")
    copied_file = []
    with open(file_name, 'r') as f:
        reader = csv.reader(f)

        headers = next(reader)
        

        for row in reader:
            copied_file.append(row)
    
    with open(history, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([])
        writer.writerow([f'{datetime.datetime.now():%d-%B-%Y %H:%M:%S}'])
        writer.writerow([])

    with open(history, "a") as f:
        writer = csv.writer(f)
        writer.writerows(copied_file)
    
    return ""
