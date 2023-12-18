from gym_functions import view_previous_workout, add_exercise, update_exercise, remove_exercise, save_exit

file_name = "exercise_list.csv"
history = "exercise_history.csv"

print("welcome to your workout tracker\n")

try:
    exercise_file = open(file_name, "r")
    exercise_file.close()
    print("Here is your last work out: ")
except FileNotFoundError:
    exercise_file = open(file_name, "w")
    exercise_file.write("exercise,weight,sets,reps\n")
    exercise_file.close()
    print("Enter 1 to add workout to your list")



def home_menu():
    print(view_previous_workout(file_name))
    print("1. Enter 1 to add new exercise")
    print("2. Enter 2 to Update exercise")
    print("3. Enter 3 to delete exercise")
    print("4. Enter 4 exit and save workout")
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