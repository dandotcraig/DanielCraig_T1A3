from gym_functions import view_previous_workout, add_exercise, update_exercise, remove_exercise, save_exit
from datetime import date
from rich import print


file_name = "exercise_list.csv"
history = "exercise_log.csv"

print("welcome to your workout tracker\n")

try:
    exercise_list = open(file_name, "r")
    exercise_list.close()
    exercise_log = open(history, "w")
    exercise_log.write(str(date.today()) + "\n")
    exercise_log.write("exercise,weight,sets,reps\n")
    exercise_log.close()
    print("Here is your last work out: ")
except FileNotFoundError:
    exercise_list = open(file_name, "w")
    exercise_list.write("exercise,weight,sets,reps\n")
    exercise_list.close()
    exercise_log = open(history, "w")
    exercise_log.write(str(date.today()) + "\n")
    exercise_log.write("exercise,weight,sets,reps\n")
    exercise_log.close()
    print("Enter 1 to add workout to your list")

print(view_previous_workout(file_name))

def home_menu():
    
    print("[blue]1. Enter 1 to add new exercise")
    print("[green]2. Enter 2 to Update exercise")
    print("[blue]3. Enter 3 to delete exercise")
    print("[green]4. Enter 4 exit and save workout")
    choice = input("Enter your selection: ")
    return choice

user_choice = ""

while user_choice != "4":
    user_choice = home_menu()
    if (user_choice == "1"):
        add_exercise(file_name)
    elif (user_choice == "2"):
        update_exercise(file_name)
    elif (user_choice == "3"):
        remove_exercise(file_name)     
    elif (user_choice == "4"):
        save_exit(file_name)
        print("Exercise saved, cya next time!")
        continue
    else:
        print("Invalid Input: ")

print("Thanks you for using workout tracker")