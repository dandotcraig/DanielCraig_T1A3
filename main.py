from gym_functions import view_previous_workout, add_exercise, update_exercise, remove_exercise, view_history, save_exit
from datetime import date
from rich import print
import emoji
import sys

print(f"You've opened { sys.argv[0]}")
file_name = "exercise_list.csv"
history = "exercise_log.csv"

print("\n[green] :flexed_biceps: Welcome to your workout tracker :flexed_biceps:  \n")

try:
    exercise_list = open(file_name, "r")
    exercise_list.close()
    exercise_log = open(history, "r")
    exercise_log.close()
    print("[blue]Here is your workout, see options below:\n")
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
    
    print("[blue]1. Enter 1 to add a new exercise")
    print("[green]2. Enter 2 to update an exercise")
    print("[blue]3. Enter 3 to remove an exercise")
    print("[green]4. Enter 4 to view your workout history")
    print("[blue]5. Enter 5 exit and log your workout")
    choice = input("\nEnter your selection: ")
    return choice

user_choice = ""

while user_choice != "5":
    user_choice = home_menu()
    if (user_choice == "1"):
        add_exercise(file_name)
    elif (user_choice == "2"):
        update_exercise(file_name)
    elif (user_choice == "3"):
        remove_exercise(file_name)   
    elif (user_choice == "4"):
        view_history(history)        
    elif (user_choice == "5"):
        save_exit(file_name, history)
        print("[green]Exercise logged, well-done, cya next time!")
        continue
    else:
        print("Invalid Input - input needs to be a number between 1 - 5 ")

print(":woozy_face:[blue]Thanks you for using workout tracker :woozy_face:")