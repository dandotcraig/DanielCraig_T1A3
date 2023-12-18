import csv

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
    exercise_name_remove = input("Enter the exercise you want to remove: ")
    exercise_list = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if (exercise_name_remove != row[0]):
                exercise_list.append(row)
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(exercise_list)

    
def add_weight(file_name):
    print("add weight")

def update_weight(file_name):
    print("update weight")

def remove_weight(file_name):
    print("remove weight")

def view_list(file_name):
    print("view list")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)