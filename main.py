from gym_functions import view_previous_workout, add_exercise, update_exercise, remove_exercise

file_name = "exercise.csv"

print("welcome to your workout tracker - what do you want to do? ")

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
    print("2. Enter 2 to add new exercise")
    print("3. Enter 3 to Update exercise")
    print("4. Enter 4 to delete exercise")
    print("5. Enter 5 exit and save workout")
    choice = input("Enter your selection: ")
    return choice

user_choice = ""

while user_choice != "5":
    user_choice = home_menu()
    if (user_choice == "1"):
        view_previous_workout(file_name)
    elif (user_choice == "2"):
        add_exercise(file_name)
    elif (user_choice == "3"):
        update_exercise(file_name)
    elif (user_choice == "4"):
        remove_exercise(file_name)     
    elif (user_choice == "5"):
        print("Exercise saved, cya next time!")
        continue
    else:
        print("Invalid Input: ")

print("Thanks you for using workout tracker")