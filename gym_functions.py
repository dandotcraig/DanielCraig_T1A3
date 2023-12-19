import csv
from datetime import date
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

    with open(file_name, 'r') as f:
        reader = csv.reader(f)   
        for row in reader:
            copied_file.append(row)
    
    print("add exercise")
    exercise_name = input("Re-type or update " + replaced_row[0] + ": ")
    weight_number = input("Re-type or update " + replaced_row[0] + ": ")
    set_number = input("Re-type or update " + replaced_row[0] + ": ")
    rep_number = input("Re-type or update " + replaced_row[0] + ": ")
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
    
    
    
    
    
    # could work
    # print("Type in the updates: ")
    # exercise_name = input("Enter rename: ")
    # weight_number = input("Enter new weight: ")
    # set_number = input("Enter new sets: ")
    # rep_number = input("Enter new reps: ")

    # exercise_list[0][0] = exercise_name
    # exercise_list[0][1] = weight_number
    # exercise_list[0][2] = set_number
    # exercise_list[0][3] = rep_number

    # print(exercise_list)

    # convert = ",".join(map(str, exercise_list[0]))

    # with open(file_name, "a") as f:
    #     writer = csv.writer(f)
    #     writer.writerow(convert)
    # end of could work
        # print(exercise_list)
    # with open(file_name, "w") as f:
        # writer = csv.writer(f)
    # for row in exercise_list:
    #     if (exercise_name_update == row[0]):
    #         print(row)
    # now we copy it over without the user input
    # with open(file_name, "
    # w") as f:
    #     writer = csv.writer(f)
    #     writer.writerows(exercise_list)

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


def view_history(file_name):
    print("Here are your previous workouts: ")

def save_exit(file_name):
    print("save & exit")






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