import csv

def view_previous_workout(file_name):
    print("view list")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def add_exercise(file_name):
    print("add exercise")
    exercise_name = input("Enter your exercise: ")
    weight_number = input("Enter your weight: ")
    set_number = input("Enter your sets: ")
    rep_number = input("Enter your reps: ")
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([exercise_name, weight_number, set_number, rep_number])

def update_exercise(file_name):
    print("update exercise")   
    

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

