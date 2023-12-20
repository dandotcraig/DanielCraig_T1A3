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
    print("add exercise")
    exercise_name = input("Enter your exercise: ")
    weight_number = input("Enter your weight: ")
    set_number = input("Enter your sets: ")
    rep_number = input("Enter your reps: ")
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([exercise_name, weight_number, set_number, rep_number])
    
    copied_file = []
    
    with open(file_name, 'r') as f:
        reader = csv.reader(f)   
        for row in reader:
            copied_file.append(row)
    print("\nhere is your updated routine")
    for i in range (len(copied_file)):
        print("Exercise " + str(int(i)) + ": " + (str(copied_file[i]))) 




def update_exercise(file_name):
    print("update exercise")
    # user input
    exercise_name_update = input("Enter the exercise you want to update: ")
    # list variable
    exercise_list = []
    # open file to read contents
    replaced_row = None

    row_num = 0
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

                
    # now we copy it over without the user input
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(exercise_list)
    
    copied_file = []
    
    print(replaced_row)
    print(row_num)

    with open(file_name, 'r') as f:
        reader = csv.reader(f)   
        for row in reader:
            copied_file.append(row)
    
    print("add exercise")
    exercise_name = input("Re-type or update " + replaced_row[0] + ": ")
    weight_number = input("Re-type or update " + replaced_row[1] + ": ")
    set_number = input("Re-type or update " + replaced_row[2] + ": ")
    rep_number = input("Re-type or update " + replaced_row[3] + ": ")
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([exercise_name, weight_number, set_number, rep_number])
    
    copied_file = []
    
    with open(file_name, 'r') as f:
        reader = csv.reader(f)   
        for row in reader:
            copied_file.append(row)
    print("\nhere is your updated routine")
    for i in range (len(copied_file)):
        print("Exercise " + str(int(i)) + ": " + (str(copied_file[i]))) 
    

def remove_exercise(file_name):
    print("remove exercise")
    # user input
    exercise_name_remove = input("Enter the exercise you want to remove: ")
    # list variable
    exercise_list = []
    # open file to read contents
    with open(file_name, "r") as f:
        # new copy of the file
        reader = csv.reader(f)
        # loop through each row
        for row in reader:
            # if its not the input
            if (exercise_name_remove != row[0]):
                # we want it in the update cvs
                exercise_list.append(row)
    # now we copy it over without the user input
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(exercise_list)
    
    copied_file = []
    
    with open(file_name, 'r') as f:
        reader = csv.reader(f)   
        for row in reader:
            copied_file.append(row)
    print("\nhere is your updated routine")
    for i in range (len(copied_file)):
        print("Exercise " + str(int(i)) + ": " + (str(copied_file[i])))
    
    return ""


def view_history(history):
    print("Here are your previous workouts: ")
    
    pull_history = []
    
    with open(history, 'r') as f:
        puller = csv.reader(f)   
        for row in puller:
            pull_history.append(row)
    
    print(pull_history)
    return ""

def save_exit(file_name, history):
    print("save & exit")
    copied_file = []
    with open(file_name, 'r') as f:
        reader = csv.reader(f)

        headers = next(reader)
        print(f"Header: {headers}")

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



    



# def view_previous_workout(file_name):
#     file = open(file_name)
#     for line in file:
#         print(line)

# def view_previous_workout(file_name):
#     print(f"Last excercise {date.today()} \n")
#     with open(file_name, "r") as f:
#         reader = csv.reader(f)
#         for row in reader:
#             print("Row" + str(row[0]) + str(row))
#             # print("\n")