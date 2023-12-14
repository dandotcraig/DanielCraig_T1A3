print("welcome to your gym tracker")

def home_menu():
    print("1. Enter 1 to add exercises to your list")
    print("2. Enter 2 to update exercises in your list")
    print("3. Enter 3 to remove exercises in your list")
    print("4. Enter 4 to view workout to your list")
    print("5. Enter 5 to view your history")
    choice = input("Enter your selection: ")
    return choice

user_choice = ""

while user_choice != "5":
    user_choice = home_menu()
    if (user_choice == "1"):
        print("You entered 1")
    elif (user_choice == "2"):
        print("You entered 2")
    elif (user_choice == "3"):
        print("You entered 3")
    elif (user_choice == "4"):
        print("You entered 4")
    elif (user_choice == "5"):
        print("You entered 5")
    else:
        print("Invalid Input: ")

print("Thanl you for using gym app!")