from gym_functions import add_exercise, update_exercise, remove_exercise, add_weight, update_weight, remove_weight, view_list

print("welcome to your gym tracker")

def home_menu():
    print("1. Enter 1 to add exercises to your list")
    print("2. Enter 2 to update exercises in your list")
    print("3. Enter 3 to remove exercises in your list")
    print("4. Enter 4 to add weight to your list")
    print("5. Enter 5 to update weight in your list")
    print("6. Enter 6 to remove weight in your list")
    print("7. Enter 7 to view workout to your list")
    print("8. Enter 8 to view your history")
    choice = input("Enter your selection: ")
    return choice

user_choice = ""

while user_choice != "8":
    user_choice = home_menu()
    if (user_choice == "1"):
        add_exercise()
    elif (user_choice == "2"):
        update_exercise()
    elif (user_choice == "3"):
        remove_exercise()
    elif (user_choice == "4"):
        add_weight()
    elif (user_choice == "5"):
        update_weight()
    elif (user_choice == "6"):
        remove_weight()
    elif (user_choice == "7"):
        view_list()      
    elif (user_choice == "8"):
        print("You entered 8")
        continue
    else:
        print("Invalid Input: ")

print("Thanl you for using gym app!")