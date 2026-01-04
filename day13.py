import json

def get_non_empty_input(prompt):
    value = input(prompt).strip()
    while not value:
        print("Input cannot be empty.")
        value = input(prompt).strip()
    return value


def get_valid_age():
    while True:
        age = input("Enter age: ")

        if not age.isdigit():
            print("Age must be a number.")
            continue

        age = int(age)

        if age < 1 or age > 120:
            print("Age must be between 1 and 120.")
            continue

        return age


def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)


users = load_users()


def add_user():
    profile = {}
    profile["name"] = get_non_empty_input("Enter name: ")
    profile["age"] = get_valid_age()
    users.append(profile)
    save_users(users)
    print("User added and saved!")


def show_users():
    if not users:
        print("No users yet.")
        return

    print("\n--- Users ---")
    for index, user in enumerate(users, start=1):
        print(f"{index}. Name: {user['name']}, Age: {user['age']}")


def edit_user():
    if not users:
        print("No users to edit.")
        return
    show_users()

    choice = input("Enter user number to edit: ")

    if not choice.isdigit():
        print("Invalid Input. ")
        return
    
    index = int(choice) - 1

    if index < 0 or index >= len(users):
        print("User number out of range. ")
        return
    
    user = users[index]

    new_name = input(f"New name ({user['name']}): ").strip()
    if new_name:
        user["name"] = new_name

    new_age = input(f"New age ({user['age']}): ").strip()
    if new_age.isdigit():
        age = int(new_age)
        if 1 <= age <= 120:
            user["age"] = age

    save_users(users)
    print("User updated successfully. ")
  
def delete_user():
    if not users:
        print("No users to delete. ")
        return
    
    show_users()

    choice = input("Enter user number to delete: ")

    if not choice.isdigit():
      print("Invalid input")
      return
    
    index = int(choice) - 1

    if index <0 or index >=len(users):
        print("User number out of range")
        return
    
    deleted_user = users.pop(index)
    save_users(users)

    print(f"Deleted User: {deleted_user['name']}")

while True:
    print("\n1. Add User")
    print("2. Show Users")
    print("3. Edit User")
    print("4. Delete User")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_user()
    elif choice == "2":
        show_users()
    elif choice == "3":
        edit_user()
    elif choice == "4":
        delete_user()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")