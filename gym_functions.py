import csv
from datetime import date
from rich import print
from tabulate import tabulate
import numpy as np

copied_file = []

def view_previous_workout(file_name):
    copied_file = []
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            copied_file.append(row)
    for i in range (len(copied_file)):
        print("Exercise " + str(int(i)) + ": " + str(copied_file[i]))
    
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
        print("Exercise " + str(int(i)) + ": " + tabulate(str(copied_file[i]))) 
    

def update_exercise(file_name):
    print("update exercise")
    # user input
    exercise_name_update = input("Enter the exercise you want to update: ")
    # list variable
    exercise_list = []
    # open file to read contents
    with open(file_name, "r") as f:
        # new copy of the file
        reader = csv.reader(f)
        for row in reader:
            exercise_list.append(row)
    
        # loop through each row
        ## for row in reader:
            # if its not the input
            ## if (exercise_name_update != row[0]):
                # we want it in the update cvs
                ## exercise_list.append(row)
    # now we copy it over without the user input
    # with open(file_name, "w") as f:
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