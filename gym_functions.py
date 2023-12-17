import csv

def add_exercise(file_name):
    print("add exercise")
    exercise_name = input("Enter your exercise: ")
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([exercise_name])

def update_exercise(file_name):
    print("update exercise")   
    

def remove_exercise(file_name):
    print("remove exercise")
    
def add_weight(file_name):
    print("add weight")
    exercise_weight = input("Enter your weight: ")
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([exercise_weight])

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